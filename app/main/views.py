from flask import render_template, abort
from . import main
from app.models import Pizza
from app.utils import get_toppings

@main.route('/')
def index():
    return render_template('index.html')

# order
@main.route('/order/<pizza_id>', methods=["GET", "POST"])
def order(pizza_id):
    '''Order pizza'''
    pizza = Pizza.query.get(pizza_id)
    toppings = get_toppings()

    if not pizza:
        return abort(404)


    return render_template('order.html', pizza=pizza, toppings=toppings)    