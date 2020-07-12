from flask import Blueprint
from . import db
from .models import Cake, CakeType, Order
import datetime


bp = Blueprint('admin', __name__, url_prefix='/admin/')

# Seed the data to database


@bp.route('/dbseed/')
def dbseed():
    caketype1 = CakeType(
        name='Parfait', description='In France, where the dish originated, parfait is made by boiling cream, egg, sugar and syrup to create a custard-like puree which is sometimes served in a parfait glass')
    caketype2 = CakeType(
        name='Cheese cake', description='Cheesecake is a sweet dessert consisting of one or more layers. The main, and thickest layer, consists of a mixture of soft, fresh cheese, eggs, and sugar.')
    caketype3 = CakeType(
        name='Cupcake', description='Cupcake is a small cake designed which may be baked in a small thin paper')
    caketype4 = CakeType(
        name='Panna cotta', description='Panna cotta is an Italian dessert of sweetened cream thickened with gelatin and molded.')

    try:
        db.session.add(caketype1)
        db.session.add(caketype2)
        db.session.add(caketype3)
        db.session.add(caketype4)
        db.session.commit()
    except:
        return 'There was an issue adding the cities in dbseed function'

    cake1 = Cake(caketype_id=caketype1.id, name='RED VELVET FRUIT PARFAIT', bestselling=True, description='The award winning worldwide cake champion in 2018 is the best seller cake in our store. This parfait is our signature and famous red velvet cake layered with blueberry glaze and garnished with crunchy muesli crumble. Delicate and irresistable dessert to complete with your favourite dish.',
                 image='cake6.jpg', dietary='Gluten Free, Peanut Free', size='10 cm diameter wide', price=12)
    cake2 = Cake(caketype_id=caketype2.id, name='CHAMPAGNE FRAISE', bestselling=True, description='Champagne fraise is one of the best seller cakes in our store. This delicate and soft chesecake is layered with yuzu cream and garnished with four different type of berries, strawberry, blueberry, raspberry and blue raspberry. The cake has always been the best-selling cake in our store since the commencement of our store',
                 image='cake5.jpg', dietary='Gluten Free', size='15 cm diameter wide', price=15)
    cake3 = Cake(caketype_id=caketype4.id, name='BERRY SWEET SLICE', bestselling=True, description='Berry Sweet Slice is one of the best seller cakes in our store. This is our signature and famous panna cotta combined with strawberry cream. This cake has accomplished the Australia Cake Award last year. Order this irresistable dessert to complete with your favourite dish.',
                 image='homepage.jpg', dietary='Gluten Free', size='9 cm wide', price=15)
    cake4 = Cake(caketype_id=caketype2.id, name='SAKURA PALETTE PASTRY', bestselling=False, description='This cheesecake is our new cake recipe in the store. It is inspired by sakura tree located in Japan. The base of the cake is the genoise cake layered with the authentic cheese from Japan, garnished with almond crumble and our favourite strawberry crumble.',
                 image='cake3.jpg', dietary='None', size='12 cm diameter wide', price=11)
    cake5 = Cake(caketype_id=caketype2.id, name='CHOCOLATE DELIGHT', bestselling=False, description='This cheese cake is our proudly made chocolate cake with 10 layers of chocolate cream. Its dough is combined with earl grey, citrus, and chocolate ganache. The flavour of the cake work so well together and it is favoured by tea lovers. Delicate and irresistable dessert to complete with your afternoon tea.',
                 image='cake4.jpg', dietary='Peanut Free', size='20 cm length and 10cm width', price=15)
    cake6 = Cake(caketype_id=caketype4.id, name='BERRY PANNACOTTA', bestselling=False, description='''Berry Pannacotta is our signature and famous panna cotta served with berry juice. Fill the air with the delicious aroma of fresh vanilla and you won't be able to wait to dive into this creamy panna cotta. Order this irresistable dessert to complete with your favourite dish.''',
                 image='cake2.jpg', dietary='Peanut Free', size='15 cm diameter wide', price=13)
    cake7 = Cake(caketype_id=caketype3.id, name='CHOCOLATE CRUMB FUZZ', bestselling=False, description='''This cupcake is our new cake recipe in the store. It is purposely created for chocolate and cheese lovers. Treat yourself with the best molten lava cake, featuring a gooey centre and a delicious, sticky scotch caramel sauce inside the cupcake. The cake is topped with sweet chocolate brownies to enhance the your satisfaction.''',
                 image='cake7.jpg', dietary='Peanut Free, Gluten Free', size='12 cm diameter wide', price=8)
    cake8 = Cake(caketype_id=caketype3.id, name='RASPBERRY VANILLA CAKE', bestselling=False, description='''This cupcake is our new cake recipe in the store. It is purposely created for vanilla and berry lovers. Treat yourself with the best berry cupcake, featuring a vanilla extract in the centre and a delicious, sticky scotch caramel puree inside the cupcake. The cake is topped with raspberry to enhance the your satisfaction.''',
                 image='cake10.jpg', dietary='Peanut Free, Gluten Free', size='13 cm diameter wide', price=10)
    cake9 = Cake(caketype_id=caketype1.id, name='CRUNCHY YOGHURT PARFAIT', bestselling=False, description='This parfait is our new cake recipe in the store. The base of the cake is the vanilla and passionfruit yoghurt layered with the crunchy almond granola, garnished with favourite strawberry. Delicate and irresistable dessert to complete with your favourite dish.',
                 image='cake9.jpg', dietary='Gluten Free', size='12 cm diameter wide', price=12)

    try:
        db.session.add(cake1)
        db.session.add(cake2)
        db.session.add(cake3)
        db.session.add(cake4)
        db.session.add(cake5)
        db.session.add(cake6)
        db.session.add(cake7)
        db.session.add(cake8)
        db.session.add(cake9)
        db.session.commit()
    except:
        return 'There was an issue adding a tour in dbseed function'

    return 'DATA LOADED'
