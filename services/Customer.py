from sqlalchemy.orm import Session
from models.models import db
from models.models import Customer

def create(customer_data):
    with Session(db.engine) as session:
        with session.begin():
            new_customer = Customer(name=customer_data["name"], email=customer_data["email"], phone=customer_data["phone"])
            session.add(new_customer)
            session.commit()

        session.refresh(new_customer)
    return new_customer

def list_all():
    with Session(db.engine) as session:
        with session.begin():
            all_cus = Customer.query.all()
            return all_cus
