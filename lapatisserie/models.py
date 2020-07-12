from . import db


# Class for cake types
class CakeType(db.Model):
    __tablename__ = 'caketypes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(500), nullable=False)
    cakes = db.relationship('Cake', backref='CakeType',
                            cascade="all, delete-orphan")

    def __repr__(self):
        str = "Id: {}, Name: {}, Description:{} \n"
        str = str.format(self.id, self.name, self.description)
        return str


# Creating class for many to many tables and incorporate quantity
class OrderDetails(db.Model):
    __tablename__ = 'orderdetails'
    order_id = db.Column(db.Integer, db.ForeignKey(
        'orders.id'), nullable=False, primary_key=True)
    cake_id = db.Column(db.Integer, db.ForeignKey(
        'cakes.id'), nullable=False, primary_key=True)
    quantity = db.Column(db.Integer, default=1)

    def __repr__(self):
        str = "OrderId: {}, CakeID: {}, Quantity:{}\n"
        str = str.format(self.order_id, self.cake_id, self.quantity)
        return str


# Class for each cake
class Cake(db.Model):
    __tablename__ = 'cakes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    bestselling = db.Column(db.Boolean, default=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(64), nullable=False)
    dietary = db.Column(db.String(150))
    size = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    caketype_id = db.Column(db.Integer, db.ForeignKey('caketypes.id'))

    def __repr__(self):
        str = "Id: {}, Name: {}, Cake Type:{}, Best Selling:{}, Description: {}, Image: {}, Dietary:{}, Size:{}, Price:{} \n"
        str = str.format(self.id, self.name, self.caketype, self.bestselling, self.description, self.image,
                         self.dietary, self.size, self.price)
        return str


# Class for order
class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    date = db.Column(db.DateTime)
    totalcost = db.Column(db.Float)
    firstname = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    email = db.Column(db.String(128))
    phone = db.Column(db.String(32))
    address = db.Column(db.String(200))
    comment = db.Column(db.String(500))
    cakes = db.relationship("Cake", secondary="orderdetails", backref="orders")

    def __repr__(self):
        str = "id: {}, Status: {}, Order date:{},  Cakes:{}, Total cost:{}, Firstname: {}, Last name: {}, Email: {}, Phone: {}, Address: {}, Comment: {}\n"
        str = str.format(self.id, self.status, self.date, self.cakes, self.total_cost,
                         self.firstname, self.lastname, self.email, self.phone, self.address, self.comment)
        return str
