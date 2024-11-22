from flask import request, jsonify
from models.schemas.CustomerSchema import customer_schema, customers_schema
from services import Customer
from marshmallow import ValidationError

def create():
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    customer_save = Customer.create(customer_data)
    return customer_schema.jsonify(customer_save), 201

def list_all():
    return customers_schema.jsonify(Customer.list_all())
