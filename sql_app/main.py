from typing import List
from fastapi import Depends, FastAPI, HTTPException, status, BackgroundTasks
from sqlalchemy.orm import Session

from . import crud, models, schemas, additional
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/titles", response_model=List[schemas.Title])
def read_titles(db: Session = Depends(get_db)):
    titles = crud.get_titles(db)
    if titles is None:
        raise HTTPException(status_code=404, detail="Titles not found")
    return titles

@app.get("/titles/{title_id}", response_model=schemas.Title)
def read_title(title_id: int, db: Session = Depends(get_db)):
    if title_id < 1:
        raise HTTPException(status_code=400, detail="Wrong title id")
    title = crud.get_title(db, title_id)
    if title is None:
        raise HTTPException(status_code=404, detail="Title not found")
    return title

@app.get("/titles_top", response_model=List[schemas.Title])
def read_titles_top(db: Session = Depends(get_db)):
    titles = crud.get_titles_top(db)
    if titles is None:
        raise HTTPException(status_code=404, detail="Titles not found")
    return titles

@app.post("/titles", response_model=schemas.Title, status_code=status.HTTP_201_CREATED)
def create_title(movie: schemas.TitleCreate, db: Session = Depends(get_db)):
    return crud.create_title(db=db, movie=movie )

@app.put("/titles/", status_code=status.HTTP_202_ACCEPTED)
def change_title(movie: schemas.Title, db: Session = Depends(get_db)):
    return crud.update_title(db, movie)

@app.delete("/titles/{title_id}")
def delete_title(title_id: int, db: Session = Depends(get_db)):
    return crud.delete_movie(db, title_id)

@app.get("/stats/")
def read_stats(db: Session = Depends(get_db)):
    return crud.get_stats(db)

@app.get("/title/and_log/{title_id}", response_model=schemas.Title)
async def read_title_and_log(title_id: int, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    if title_id < 1:
        raise HTTPException(status_code=400, detail="Wrong title id")
    title = crud.get_title(db, title_id)
    if title is None:
        raise HTTPException(status_code=404, detail="Title not found")
    background_tasks.add_task(additional.write_log_to_file, message=str(title_id))
    return title

@app.get("/title/with_people/{title_id}")
def read_title_with_people(title_id: int, db: Session = Depends(get_db)):
    if title_id < 1:
        raise HTTPException(status_code=400, detail="Wrong title id")
    title = crud.get_title_with_people(db, title_id)
    if title is None:
        raise HTTPException(status_code=404, detail="Title not found")    
    if title.people == []:
        raise HTTPException(status_code=404, detail="No people for this title")
    return title