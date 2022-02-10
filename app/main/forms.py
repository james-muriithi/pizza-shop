from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import input_required

class OrderForm(FlaskForm):
    topping = StringField("Topping", validators=[input_required("Topping is required")])
    quantity = IntegerField("Quantity", validators=[input_required("Quantity is required")])   