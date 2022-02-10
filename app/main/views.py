from unicodedata import name
from . import main
from flask import render_template,redirect,url_for,request,flash,abort
from .forms import PizzaForm
from ..models import Pizza
from .. import db,photos

@main.route('/')
def index():
    all_pizzas=Pizza.query.all()
    return render_template('index.html',all_pizzas=all_pizzas)

@main.route('/add',methods = ["GET","POST"])
def add():
    """Add pizza function"""
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
def edit(id):
    """Edit pizza function"""

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
def delete(id):
    """Delete pizza function"""
    data=Pizza.query.get(id)
    db.session.delete(data)
    db.session.commit()

    flash("Pizza successfully deleted")

    return redirect(url_for(".index"))

    
    



