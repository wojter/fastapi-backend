from sqlalchemy.orm import Session
from . import models, schemas


def get_titles(db: Session):
    return db.query(models.Title).all()


def get_title(db: Session, title_id: int):
    return db.query(models.Title).filter(models.Title.id == title_id).first()


def create_title(db: Session, movie: schemas.TitleCreate):
    # db_movie = models.Title(title=movie.title, type=movie.type, description=movie.description,
    #                         release_year=movie.release_year, runtime=movie.runtime)
    db_movie = models.Title(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)

    return db_movie