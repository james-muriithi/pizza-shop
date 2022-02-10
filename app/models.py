
from . import db
from datetime import datetime
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(255))

    orders = db.relationship('Order', backref="user", lazy="dynamic")


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    users = db.relationship('User', backref="role", lazy="dynamic")


class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Integer)
    size = db.Column(db.String(64))
    image = db.Column(db.String(255))
    description = db.Column(db.Text)

    orders = db.relationship('Order', backref="pizza", lazy="dynamic")

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pizza_id = db.Column(db.Integer,db.ForeignKey('pizzas.id'))
    topping = db.Column(db.String(64))
    total = db.Column(db.Integer)

    created_at = db.Column(db.DateTime, index=True, default=datetime.now)