from flask import Blueprint
from controllers.Customer import create, list_all

customer_blueprint = Blueprint('customer_bp', __name__)
customer_blueprint.route('/add', methods=['POST'])(create)
customer_blueprint.route('/', methods=['GET'])(list_all)
