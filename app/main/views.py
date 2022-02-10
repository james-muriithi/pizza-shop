from unicodedata import name
from . import main
from flask import render_template,redirect,url_for,request,flash,abort
from .forms import PizzaForm, OrderForm
from ..models import Pizza, Order
from .. import db,photos
from . import main
from app.utils import Toppings
from app.email import mail_message
from flask_login import current_user, login_required


@main.route('/')
def index():
    all_pizzas=Pizza.query.all()
    return render_template('index.html',all_pizzas=all_pizzas)

@main.route('/add',methods = ["GET","POST"])
@login_required
def add():
    """Add pizza function"""
    if not current_user.is_admin:
        abort(403)

    all_pizzas=Pizza.query.all()

    if request.method=='POST':
        pizza_name=request.form['name']
        pizza_price=request.form['price']
        pizza_size=request.form['size']
        pizza_description=request.form['description']
        new_pizza =Pizza(name=pizza_name,price=pizza_price,size=pizza_size,description=pizza_description)
        if 'image' in request.files:
            filename = photos.save(request.files['image'])
            path = f'photos/{filename}'
            new_pizza.image = path
            db.session.commit()

        db.session.add(new_pizza)
        db.session.commit()
        flash("Pizza added successfully")
        return redirect(url_for(".index")) 

    return render_template('CRUD/create.html')


@main.route('/pizza/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    """Edit pizza function"""
    if not current_user.is_admin:
        abort(403)

    all_data=Pizza.query.get(id)
    if request.method=='POST':        
        all_data.name=request.form['name']
        all_data.price=request.form['price']
        all_data.size=request.form['size']
        all_data.description=request.form['description']
        # all_data.image=request.form['image']

        db.session.commit()
        flash("Pizza successfully updated")
        return redirect(url_for(".index"))

    return render_template("CRUD/update.html", data=all_data)


@main.route('/delete/<id>',methods=["GET","POST"])
@login_required
def delete(id):
    """Delete pizza function"""
    if not current_user.is_admin:
        abort(403)

    data=Pizza.query.get(id)
    db.session.delete(data)
    db.session.commit()

    flash("Pizza successfully deleted")

    return redirect(url_for(".index"))
  

# order
@main.route('/order/<pizza_id>', methods=["GET", "POST"])
@login_required
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

        order = Order(total=total, pizza=pizza, quantity = form.quantity.data, topping=form.topping.data, user=current_user)

        db.session.add(order)
        db.session.commit()

        #send email to user
        mail_message("Order Successsful","email/order-success",current_user.email,user=current_user)

        return redirect(url_for('.order_success', order_id = order.id))

    return render_template('order.html', pizza=pizza, toppings=toppings, form=form)    


@main.route('/order-success/<order_id>', methods=["GET"])
@login_required
def order_success(order_id):
    order = Order.query.get(order_id)
    if not order:
        return abort(404)
        
    return render_template('order-success.html', order=order)   
