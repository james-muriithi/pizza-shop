from flask import render_template, abort
from . import main
from ..models import Pizza

@main.route('/')
def index():
    return render_template('index.html')

# order
@main.route('/order/<pizza_id>', methods=["GET", "POST"])
def order(pizza_id):
    '''Order pizza'''
    pizza = Pizza.query.get(pizza_id)

    if not pizza:
        return abort(404)


    return render_template('order.html', pizza=pizza)    