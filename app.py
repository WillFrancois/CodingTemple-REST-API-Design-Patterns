from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from models.models import db
from schema import ma

from routes.Customer import customer_blueprint
from routes.Employee import employee_blueprint
from routes.Product import product_blueprint
from routes.Order import order_blueprint
from routes.Production import production_blueprint

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["50 per hour"],
    storage_uri="memory://",
)

def blueprints(app):
    app.register_blueprint(customer_blueprint, url_prefix='/customers')
    app.register_blueprint(employee_blueprint, url_prefix='/employees')
    app.register_blueprint(product_blueprint, url_prefix='/products')
    app.register_blueprint(order_blueprint, url_prefix='/orders')
    app.register_blueprint(production_blueprint, url_prefix='/productions')

blueprints(app)
db.init_app(app)
ma.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

if __name__ == '__main__':
    app.run()
