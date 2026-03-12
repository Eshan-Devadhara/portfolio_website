from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user, login_required
from app import db
from app.models import User, ContactMessage, Project

admin = Blueprint('admin', __name__)

@admin.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user is None or not user.check_password(password):
            flash('Invalid username or password')
            return redirect(url_for('admin.login'))
        
        login_user(user)
        return redirect(url_for('admin.dashboard'))
        
    return render_template('admin/login.html')

@admin.route('/dashboard')
@login_required
def dashboard():
    messages = ContactMessage.query.order_by(ContactMessage.timestamp.desc()).all()
    return render_template('admin/dashboard.html', messages=messages)

@admin.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))