from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from .models import Cake, CakeType, Order, OrderDetails
from datetime import datetime
from .forms import CheckoutForm
from . import db

bp = Blueprint('main', __name__)


# Creating context to update quantity to navbar for all templates
@bp.context_processor
def cartquantity():
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        return dict(quantity=len(order.cakes))
    else:
        return dict(quantity=0)


# About Page
@bp.route('/about')
def about():
    # Call the function in context_processor to show cart quantity in navbar
    result = cartquantity()
    return render_template('about.html', cartquantity=result['quantity'])


# Home Page
@bp.route('/')
def index():
    cakes = Cake.query.order_by(Cake.name).all()
    bestselling = Cake.query.filter(Cake.bestselling == True)
    # Call the function in context_processor to show cart quantity in navbar
    result = cartquantity()
    return render_template('index.html', cakes=cakes, bestselling=bestselling, cartquantity=result['quantity'])


# Detail Page
@bp.route('/cakes/<int:cakeid>/')
def detail(cakeid):
    cake = Cake.query.filter(Cake.id == cakeid).one()
    # Call the function in context_processor to show cart quantity in navbar
    result = cartquantity()
    return render_template('detail.html', cake=cake, cartquantity=result['quantity'])


# Search cake in home page
@bp.route('/search/')
def search():
    search = request.args.get('search')
    search = '%{}%'.format(search)
    cakes = Cake.query.filter(Cake.description.like(search)).all()
    # Call the function in context_processor to show cart quantity in navbar
    result = cartquantity()
    return render_template('index.html', cakes=cakes, cartquantity=result['quantity'])


# Filter cake in home page
@bp.route('/filtercake/')
def filtercake():
    caketype = request.args.get('caketype')
    if (caketype == 'All cakes'):
        cakes = Cake.query.order_by(Cake.name).all()
    else:
        cakes = db.session.query(Cake).select_from(Cake).join(
            CakeType).filter(CakeType.name == caketype)
    # Call the function in context_processor to show cart quantity in navbar
    result = cartquantity()
    return render_template('index.html', cakes=cakes, cartquantity=result['quantity'])


# Making order
@bp.route('/order', methods=['POST', 'GET'])
def order():
    cake_id = request.values.get('cake_id')

    # retrieve order if there is one
    if 'order_id' in session.keys():
        order = Order.query.get(session['order_id'])
    else:
        # there is no order
        order = None

    # create new order if needed
    if order is None:
        order = Order(status=False, date=datetime.now(), totalcost=0,
                      firstname='', surname='', email='', phone='', address='', comment='')
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.id
        except:
            print('failed at creating a new order')
            order = None

    # calcultate totalprice and add quantity for each cake to a list to show in order page
    totalprice = 0
    quantities = []
    if order is not None:
        for cake in order.cakes:
            quantity = OrderDetails.query.get_or_404(
                [order.id, cake.id]).quantity
            totalprice = totalprice + quantity*cake.price
            quantities.append(quantity)

    # are we adding an item?
    if cake_id is not None and order is not None:
        cake = Cake.query.get(cake_id)
        if cake not in order.cakes:
            try:
                order.cakes.append(cake)
                db.session.commit()
                flash('Cake has been added to the cart')
            except:
                return 'There was an issue adding the item to your basket'
            return redirect(url_for('main.index', _anchor='search_anchor'))
        else:
            item = OrderDetails.query.get_or_404([order.id, cake_id])
            item.quantity += 1
            db.session.commit()
            flash('Quantity has been added to the cart')
            return redirect(url_for('main.index', _anchor='search_anchor'))

    # Call the function in context_processor to show cart quantity
    result = cartquantity()

    return render_template('order.html', order=order, totalprice=totalprice, quantities=quantities, cartquantity=result['quantity'])


# Delete specific basket items
@bp.route('/deleteorderitem', methods=['POST'])
def deleteorderitem():
    id = request.form['cake_id']
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        cake_to_delete = Cake.query.get(id)
        try:
            order.cakes.remove(cake_to_delete)
            db.session.commit()
            return redirect(url_for('main.order'))
        except:
            return 'Problem deleting item from order'
    return redirect(url_for('main.order'))


# Delete Order
@bp.route('/deleteorder')
def deleteorder():
    if 'order_id' in session:
        del session['order_id']
        flash('All items has been deleted from your cart')
    return redirect(url_for('main.index', _anchor='search_anchor'))


# Checkout Page
@bp.route('/checkout', methods=['POST', 'GET'])
def checkout():
    form = CheckoutForm()
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        if not order.cakes:
            flash(
                'No cakes have been selected. Please add cakes to cart before checkout.')
            return redirect(url_for('main.order'))

        if form.validate_on_submit():
            order.status = True
            order.firstname = form.firstname.data
            order.surname = form.surname.data
            order.email = form.email.data
            order.phone = form.phone.data
            order.address = form.address.data
            order.comment = form.comment.data

            # Calculate total cost
            totalcost = 0
            for cake in order.cakes:
                quantity = OrderDetails.query.get_or_404(
                    [order.id, cake.id]).quantity
                totalcost = totalcost + quantity*cake.price
            order.totalcost = totalcost
            order.date = datetime.now()
            try:
                db.session.commit()
                del session['order_id']
                flash(
                    'Thank you! We will contact you soon...')
                return redirect(url_for('main.index', _anchor='search_anchor'))
            except:
                return 'There was an issue completing your order'
        # Call the function in context_processor to show cart quantity in navbar
        result = cartquantity()
    return render_template('checkout.html', form=form, cartquantity=result['quantity'])
