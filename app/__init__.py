from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login = LoginManager()
login.login_view = 'admin.login'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login.init_app(app)

    # Register Main Routes
    from app.routes import main
    app.register_blueprint(main)

    # Register Admin Routes
    from app.admin_routes import admin
    app.register_blueprint(admin, url_prefix='/admin')
    
    # Load User for Flask-Login
    from app.models import User
    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app