from sqlalchemy.orm import Session
from models.models import db
from models.models import Production

def create(production_data):
    with Session(db.engine) as session:
        with session.begin():
            new_production = Production(product_id=production_data["product_id"], quantity_produced=production_data["quantity_produced"], date_produced=production_data["date_produced"])
            session.add(new_production)
            session.commit()

        session.refresh(new_production)
    return new_production

def list_all():
    with Session(db.engine) as session:
        with session.begin():
            all_production = Production.query.all()
            return all_production
