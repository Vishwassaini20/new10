from flask import Blueprint, render_template, redirect, url_for, request, session
from app import db  # Avoid circular import
from .models import User, Subject, Chapter, Quiz, Question, Score
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':  # Simple admin login check
            session['admin'] = True
            return redirect(url_for('main.admin_dashboard'))
    return render_template('admin_login.html')

@main.route('/admin/dashboard')
def admin_dashboard():
    if 'admin' in session:
        subjects = Subject.query.all()
        return render_template('admin_dashboard.html', subjects=subjects)
    return redirect(url_for('main.admin_login'))

@main.route('/admin/subjects', methods=['GET', 'POST'])
def manage_subjects():
    if 'admin' in session:
        if request.method == 'POST':
            name = request.form['name']
            description = request.form['description']
            subject = Subject(name=name, description=description)
            db.session.add(subject)
            db.session.commit()
            return redirect(url_for('main.admin_dashboard'))
        return render_template('manage_subjects.html')
    return redirect(url_for('main.admin_login'))

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        full_name = request.form['full_name']
        qualification = request.form['qualification']
        dob = request.form['dob']
        user = User(username=username, password=password, full_name=full_name, qualification=qualification, dob=datetime.strptime(dob, '%Y-%m-%d'))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.login'))
    return render_template('register.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['user_id'] = user.id
            return redirect(url_for('main.user_dashboard'))
    return render_template('login.html')

@main.route('/user/dashboard')
def user_dashboard():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        subjects = Subject.query.all()
        return render_template('user_dashboard.html', user=user, subjects=subjects)
    return redirect(url_for('main.login'))