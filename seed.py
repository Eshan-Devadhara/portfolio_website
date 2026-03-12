from app import create_app, db
from app.models import Project, Skill, User

app = create_app()

def seed_data():
    with app.app_context():
        # Create tables if they don't exist
        db.create_all()

        # --- 1. ADMIN USER ---
        # Check if admin already exists
        if not User.query.filter_by(username='admin').first():
            print("Creating Admin User...")
            admin = User(username='admin')
            admin.set_password('admin123') 
            db.session.add(admin)

        # --- 2. PROJECTS DATA ---
        # Check if projects exist to avoid duplicates
        if not Project.query.first():
            print("Seeding Projects...")
            projects = [
                # CS Projects
                Project(title="AI Defense System", description="Computer vision system for identifying unauthorized drones in restricted airspace.", category="cs", technologies="Python, TensorFlow, OpenCV"),
                Project(title="Portfolio Web App", description="Responsive single-page application with dynamic theme switching and Postgres backend.", category="cs", technologies="Flask, PostgreSQL, Tailwind"),
                
                # CAD Projects
                Project(title="Quadcopter Frame V2", description="Aerodynamic frame design optimized for durability and weight.", category="cad", technologies="SolidWorks", image_url="https://images.unsplash.com/photo-1527606308472-358ad7210e3f?w=800"),
                Project(title="USV Hull Design", description="Autonomous Unmanned Surface Vehicle hull for autonomous water navigation.", category="cad", technologies="Fusion 360", image_url="https://images.unsplash.com/photo-1628126235206-526053784c45?w=800"),

                # Graphics Projects
                Project(title="UI Kit Design", description="Comprehensive UI component library for fintech applications.", category="graphics", technologies="Figma"),
                Project(title="App Prototype", description="High-fidelity mobile app prototype with interactive user flows.", category="graphics", technologies="Adobe XD"),
            ]
            db.session.add_all(projects)

        # --- 3. SKILLS DATA ---
        # Clear existing skills to prevent duplicates when re-seeding
        Skill.query.delete()
        
        print("Seeding Skills...")
        skills = [
            # Programming
            Skill(name="Python", category="programming", proficiency=90, icon_class="fa-brands fa-python"),
            Skill(name="C++", category="programming", proficiency=80, icon_class="fa-solid fa-code"),
            Skill(name="JavaScript", category="programming", proficiency=85, icon_class="fa-brands fa-js"),
            Skill(name="SQL", category="programming", proficiency=85, icon_class="fa-solid fa-database"),

            # Web Development
            Skill(name="HTML", category="web_dev", proficiency=95, icon_class="fa-brands fa-html5"),
            Skill(name="CSS", category="web_dev", proficiency=90, icon_class="fa-brands fa-css3-alt"),
            Skill(name="JS (ES6+)", category="web_dev", proficiency=85, icon_class="fa-brands fa-js-square"),
            Skill(name="PERN Stack", category="web_dev", proficiency=80, icon_class="fa-solid fa-layer-group"),
            Skill(name="Flask", category="web_dev", proficiency=85, icon_class="fa-solid fa-flask"),
            Skill(name="PHP", category="web_dev", proficiency=70, icon_class="fa-brands fa-php"),

            # Databases
            Skill(name="MySQL", category="databases", icon_class="fa-solid fa-database"),
            Skill(name="PostgreSQL", category="databases", icon_class="fa-solid fa-server"),
            Skill(name="MongoDB", category="databases", icon_class="fa-solid fa-leaf"),

            # Tools
            Skill(name="Git", category="tools", icon_class="fa-brands fa-git-alt"),
            Skill(name="Linux", category="tools", icon_class="fa-brands fa-linux"),
            Skill(name="Fusion 360", category="tools", icon_class="fa-solid fa-cube"),
            Skill(name="Adobe Illustrator", category="tools", icon_class="fa-solid fa-pen-nib"),
            Skill(name="Figma", category="tools", icon_class="fa-brands fa-figma"),
            Skill(name="Microsoft 360", category="tools", icon_class="fa-brands fa-microsoft"),
        ]

        db.session.add_all(skills)
        db.session.commit()
        
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_data()