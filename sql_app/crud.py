from sqlalchemy.orm import Session
from sqlalchemy import func

from . import models, schemas

def get_titles(db: Session):
    return db.query(models.Titles).all()


def get_title(db: Session, title_id: int):
    return db.query(models.Titles).filter(models.Titles.id == title_id).first()

def get_title_with_people(db: Session, title_id: int):
    title = db.query(models.Titles).join(models.Person).filter(models.Titles.id == title_id).first()
    if hasattr(title, 'people'):
        t = title.people
    else:
        title = db.query(models.Titles).filter(models.Titles.id == title_id).first()
    return title

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
    title_avg_runtime_by_year = db.query(models.Titles.release_year, func.avg(
        models.Titles.runtime)).group_by(models.Titles.release_year)
    title_count_by_year = db.query(models.Titles.release_year, func.count(
        models.Titles.id)).group_by(models.Titles.release_year)

    return {"movies_genres": movie_shows_count, "avg_runtime_by_year": title_avg_runtime_by_year,
            "count_title_by_rel_year": title_count_by_year}
