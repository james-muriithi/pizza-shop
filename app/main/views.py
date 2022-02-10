from flask import render_template, abort, redirect, url_for
from . import main
from app import db
from app.models import Order, Pizza
from app.utils import Toppings
from .forms import OrderForm
from app.email import mail_message

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

        #send email to user
        # mail_message("Order Successsful","email/order-success",current_user.email,user=current_user)

        return redirect(url_for('.order_success', order_id = order.id))

    return render_template('order.html', pizza=pizza, toppings=toppings, form=form)    


@main.route('/order-success/<order_id>', methods=["GET"])
def order_success(order_id):
    order = Order.query.get(order_id)
    if not order:
        return abort(404)
        
    return render_template('order-success.html', order=order)    