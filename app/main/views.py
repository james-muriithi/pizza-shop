from flask import render_template, abort
from . import main
from app import db
from app.models import Order, Pizza
from app.utils import Toppings, get_toppings
from .forms import OrderForm

@main.route('/')
def index():
    return render_template('index.html')

# order
@main.route('/order/<pizza_id>', methods=["GET", "POST"])
def order(pizza_id):
    '''Order pizza'''
    pizza = Pizza.query.get(pizza_id)
    form = OrderForm()
    toppings = Toppings.get_toppings()
    if not pizza:
        return abort(404)

    if form.validate_on_submit():
        topping_price = int(Toppings.get_topping(form.topping.data).price)
        total = (int(pizza.price) + topping_price) * int(form.quantity.data)

        order = Order(total=total, pizza=pizza, quantity = form.quantity.data, topping=form.topping.data)

        db.session.add(order)
        db.session.commit()

        return "saved successfully"
        

    return render_template('order.html', pizza=pizza, toppings=toppings, form=form)    