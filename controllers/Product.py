from flask import request, jsonify
from models.schemas.ProductSchema import product_schema, products_schema
from services import Product
from marshmallow import ValidationError

def create():
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    product_save = Product.create(product_data)
    return product_schema.jsonify(product_save), 201

def list_all():
    return products_schema.jsonify(Product.list_all())
