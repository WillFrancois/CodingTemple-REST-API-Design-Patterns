from flask import Blueprint
from controllers.Production import create, list_all

production_blueprint = Blueprint('production_bp', __name__)
production_blueprint.route('/add', methods=['POST'])(create)
production_blueprint.route('/', methods=['GET'])(list_all)
