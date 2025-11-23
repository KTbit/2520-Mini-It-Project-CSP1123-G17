from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from databasemodels import db, User, SavedRecipe #shopping list db to be made by Salman
from config import Config
from utilities import search_recipes_by_ingredients, get_recipe_details #shopping list...nutrition / scaling calculator wip

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# creating the database tables
with app.app_context():
    db.create_all()

# Public route(s)

@app.route('/')
def index():
    return render_template('index.html')

# User authentication (logging in/out, registering) routes

@app.route('/register', methods=['GET', 'POST'])
def  user_register():
    if current_user.is_authenticated:
        return redirect(url_for('user_dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # check if username exists...
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'danger')
            return redirect(url_for('user_register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'danger')
            return redirect(url_for('user_register'))
    
        # for registering new users into the system
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('user_login'))
    
    return render_template('user/user_register.html')

@app.route('/login', methods=['GET', 'POST'])
def user_login(): 
    if current_user.is_authenticated:
        return redirect(url_for('user_dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            flash('Login successful!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('user_dashboard'))
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('user/user_login.html')

@app.route('/logout')
@login_required
def user_logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

# User dashboard route

@app.route('/dashboard')
@login_required
def user_dashboard():
    saved_recipes = SavedRecipe.query.filter_by(user_id=current_user.id).all()
    return render_template('user/userdashboard.html', saved_recipes=saved_recipes)

# Recipes route

@app.route('/recipes/browse')
def recipe_browse():
    # to add recipe browsing logic
    return render_template('recipe_section/recipebrowse.html')

@app.route('/recipes/<int:recipe_id>')
def recipe_detail(recipe_id):
    # to add recipe detail logic
    return render_template('recipe_section/recipedetail.html', recipe_id=recipe_id)

#admin routes

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if current_user.is_authenticated and current_user.is_admin:
        return redirect(url_for('admin_dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password) and user.is_admin:
            login_user(user)
            flash('Admin login successful!', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid admin credentials', 'danger')
    
    return render_template('admin/admin_login.html')

#admin route(s) WIP - maybe admins can register / add new admins under their supervision(?)

@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        flash('Access denied. Admin only.', 'danger')
        return redirect(url_for('index'))
    
    users = User.query.all()
    return render_template('admin/admin_registration.html', users=users)

# for admin registration

@app.route('/admin/register', methods=['GET', 'POST'])
@login_required
def admin_register():
    if not current_user.is_admin:
        flash('Access denied. Admin only.', 'danger')
        return redirect(url_for('index'))
    
    return render_template('admin/admin_registration.html')

# run the app

if __name__ == '__main__':
    app.run(debug=True)


