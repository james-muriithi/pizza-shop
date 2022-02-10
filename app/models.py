from flask import url_for
import os
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import db

from . import login_manager

from . import db
from datetime import datetime

class User(db.Model,UserMixin):
    #...
    '''
    User tables
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(255),unique = True,index = True)
    name = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    orders = db.relationship("Order", backref="user", lazy="dynamic")
   
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @property
    def is_admin(self):
        return self.role_id == 1  

    @property
    def first_name(self):
        return self.name.split()[0]    

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    @login_manager.user_loader
    def load_user(user_id):
      return User.query.get(int(user_id))

    def __repr__(self):
        return f"User {self.name}"


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    users = db.relationship('User', backref="role", lazy="dynamic")

    def __repr__(self):
        return f"Role {self.name}"


class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Integer)
    size = db.Column(db.String(64))
    image = db.Column(db.String(255))
    description = db.Column(db.Text)

    orders = db.relationship('Order', backref="pizza", lazy="dynamic")

    @property
    def pizza_image(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        if self.image and os.path.isfile(current_dir + url_for('static', filename=self.image)):
            return url_for('static', filename=self.image)
        return url_for('static', filename="images/pizza4.jpg")

    def __repr__(self):
        return f"Pizza {self.name}"

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pizza_id = db.Column(db.Integer,db.ForeignKey('pizzas.id'))
    topping = db.Column(db.String(64))
    total = db.Column(db.Integer)
    quantity = db.Column(db.Integer)

    created_at = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return f"Order {self.id}"
