from sqlalchemy.orm import Session
from models.models import db
from models.models import Product

def create(product_data):
    with Session(db.engine) as session:
        with session.begin():
            new_product = Product(name=product_data["name"], price=product_data["price"])
            session.add(new_product)
            session.commit()

        session.refresh(new_product)
    return new_product

def list_all():
    with Session(db.engine) as session:
        with session.begin():
            all_prod = Product.query.all()
            return all_prod
