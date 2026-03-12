from flask import Blueprint, render_template, request, flash, redirect, url_for
from app import db
from app.models import Project, Skill, ContactMessage

main = Blueprint('main', __name__)

@main.route('/')
def home():
    # Fetch data from PostgreSQL
    projects = Project.query.all()
    skills = Skill.query.all()
    
    # Filter projects for the template
    graphics_projects = [p for p in projects if p.category == 'graphics']
    cs_projects = [p for p in projects if p.category == 'cs']
    cad_projects = [p for p in projects if p.category == 'cad']
    
    return render_template('home.html', 
                         graphics_projects=graphics_projects,
                         cs_projects=cs_projects,
                         cad_projects=cad_projects,
                         skills=skills)

@main.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject') or "Portfolio Inquiry"
    message_content = request.form.get('message')
    
    if name and email and message_content:
        new_message = ContactMessage(
            name=name, 
            email=email, 
            subject=subject, 
            message=message_content
        )
        db.session.add(new_message)
        db.session.commit()
        
    # Redirect back to home anchor
    return redirect(url_for('main.home', _anchor='contact'))