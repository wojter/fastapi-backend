from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models, schemas


def get_titles(db: Session):
    return db.query(models.Titles).all()


def get_title(db: Session, title_id: int):
    return db.query(models.Titles).filter(models.Titles.id == title_id).first()


def get_titles_top(db: Session):
    return db.query(models.Titles).limit(10).all()


def create_title(db: Session, movie: schemas.TitleCreate):
    db_movie = models.Titles(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie


def update_title(db: Session, movie: schemas.Title):
    db_movie = db.query(models.Titles).filter(
        models.Titles.id == movie.id).first()
    for k, v in movie.dict().items():
        setattr(db_movie, k, v)
    db.commit()
    return db.query(models.Titles).filter(models.Titles.id == movie.id).first()


def delete_movie(db: Session, title_id: int):
    try:
        db.query(models.Titles).filter(models.Titles.id == title_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)
    return {"delete status": "success"}


def get_stats(db: Session):
    movie_shows_count = db.query(models.Titles.type, func.count(
        models.Titles.type)).group_by(models.Titles.type)
    return movie_shows_count
