from sqlalchemy.orm import Session
from . import models, schemas

def get_all(db: Session):
    return db.query(models.Title).all()