from app import app, db
from databasemodels import User

with app.app_context():
    username = input("Enter admin username: ")
    email = input("Enter admin email: ")
    password = input("Enter admin password: ")
    
    if User.query.filter_by(username=username).first():
        print("❌ Username already exists!")
    else:
        admin = User(username=username, email=email, is_admin=True)
        admin.set_password(password)
        db.session.add(admin)
        db.session.commit()
        print(f"✅ Admin user '{username}' created successfully!")