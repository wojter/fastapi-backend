from sqlalchemy.orm import Session
from . import models, schemas


def get_titles(db: Session):
    return db.query(models.Titles).all()


def get_title(db: Session, title_id: int):
    return db.query(models.Titles).filter(models.Titles.id == title_id).first()


def create_title(db: Session, movie: schemas.TitleCreate):
    db_movie = models.Titles(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def update_title(db: Session, movie: schemas.Title):
    db_movie = db.query(models.Titles).filter(models.Titles.id == movie.id).first()
    for k, v in movie.dict().items():
        setattr(db_movie, k, v)
    db.commit()   
    return db.query(models.Titles).filter(models.Titles.id == movie.id).first()
