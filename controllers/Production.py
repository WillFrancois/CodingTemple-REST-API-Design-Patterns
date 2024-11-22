from flask import request, jsonify
from models.schemas.ProductionSchema import production_schema, productions_schema
from services import Production
from marshmallow import ValidationError

def create():
    try:
        production_data = production_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    production_save = Production.create(production_data)
    return production_schema.jsonify(production_save), 201

def list_all():
    return productions_schema.jsonify(Production.list_all())
