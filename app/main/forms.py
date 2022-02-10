from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import input_required
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField, SelectField, PasswordField, IntegerField, FileField
from wtforms.validators import input_required

sizes = ['select pizza size','small', 'medium', 'large']


class PizzaForm(FlaskForm):
    name = StringField('Pizza name', validators=[input_required(message="Name required")],
                       render_kw={"placeholder": "Pizza name"})
    price = IntegerField('Pizza price', validators=[input_required(message="Pizza price required")],
                         render_kw={"placeholder": "Pizza price"})
    size = SelectField('Pizza size', validators=[input_required(message="Pizza size required")], choices=sizes)
    description = TextAreaField('Pizza description', validators=[input_required(message="Description required")],
                                render_kw={"placeholder": "Pizza description"})
    # image = FileField('Image File',validators=[input_required()] )
    submit = SubmitField("Add Pizza")

class OrderForm(FlaskForm):
    topping = StringField("Topping", validators=[input_required("Topping is required")])
    quantity = IntegerField("Quantity", validators=[input_required("Quantity is required")])