from sqlalchemy.orm import Session
from . import models, schemas


def get_titles(db: Session):
    return db.query(models.Titles).all()


def get_title(db: Session, title_id: int):
    return db.query(models.Titles).filter(models.Titles.id == title_id).first()


def create_title(db: Session, movie: schemas.TitleCreate):
    # db_movie = models.Titles(title=movie.title, type=movie.type, description=movie.description,
    #                         release_year=movie.release_year, runtime=movie.runtime)
    db_movie = models.Titles(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)

    return db_movie

def update_title(db: Session, movie: schemas.Title):
    db_movie = db.query(models.Titles).filter(models.Titles.id == movie.id).first()
    # db_movie.title = movie.title
    # db_movie.description = movie.description
    # db_movie.type = movie.type
    # db_movie.release_year = movie.release_year
    # db_movie.runtime = movie.runtime
    for k, v in movie.dict().items():
        setattr(db_movie, k, v)
    db.commit()
        
    return db.query(models.Titles).filter(models.Titles.id == movie.id).first()
