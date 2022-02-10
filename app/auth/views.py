from crypt import methods
from flask import render_template
from . import auth
from flask import render_template,redirect,url_for
from ..models import User
from .forms import SignupForm, LoginForm
from .. import db

@auth.route('/signup',methods = ["GET","POST"])
def register():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, name = form.name.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('signup.html',signup_form = form)

@auth.route('/login', methods = ['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('login.html',login_form = form)

   