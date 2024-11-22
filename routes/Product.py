from flask import Blueprint
from controllers.Product import create, list_all

product_blueprint = Blueprint('product_bp', __name__)
product_blueprint.route('/add', methods=['POST'])(create)
product_blueprint.route('/', methods=['GET'])(list_all)
