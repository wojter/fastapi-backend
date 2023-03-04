from sqlalchemy.orm import Session
from . import models, schemas

def get_titles(db: Session):
    return db.query(models.Title).all()

def get_title(db: Session, title_id: int):
    return db.query(models.Title).filter(models.Title.id == title_id).first()
