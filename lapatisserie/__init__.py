from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


db = SQLAlchemy()
app = Flask(__name__)


def create_app():
    app.debug = True
    app.secret_key = 'LapatisEri32020'

    # set the app configuration data
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lapatisserie.sqlite'

    # initialize db with flask app
    db.init_app(app)

    bootstrap = Bootstrap(app)

    # importing modules here to avoid circular references, register blueprints of routes
    from . import views
    app.register_blueprint(views.bp)

    # To seed the database
    # from . import admin
    # app.register_blueprint(admin.bp)

    return app


@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):
    return render_template("404.html")


@app.errorhandler(500)
def internal_error(e):
    return render_template("500.html")
