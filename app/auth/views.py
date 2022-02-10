from . import auth
from flask import render_template,redirect,url_for, request, flash
from ..models import Role, User
from .forms import SignupForm, LoginForm
from .. import db
from flask_login import login_user, login_required, logout_user
from ..email import mail_message

@auth.route('/signup',methods = ["GET","POST"])
def register():
    form = SignupForm()
    if form.validate_on_submit():
        role = Role.query.get(2)
        user = User(email=form.email.data, password=form.password.data, name=form.name.data, role=role)
        db.session.add(user)
        db.session.commit()
        
        # send email to user
        mail_message("Welcome to Pitches","email/welcome_user",user.email,user=user)


        flash('User Account created successfully!', 'success')
        login_user(user)
        return redirect(request.args.get('next') or url_for('main.index'))

    return render_template('signup.html',form = form)

@auth.route('/login', methods = ['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or Password', 'danger')
    return render_template('login.html',form = form)

   
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))