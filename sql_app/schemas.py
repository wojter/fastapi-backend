from typing import Union
from pydantic import BaseModel

class TitleBase(BaseModel):
    title: str
    type: str
    description: Union[str, None] = None
    runtime: Union[int, None] = None
    release_year: Union[int, None] = None

class TitleCreate(TitleBase):
    pass

class Title(TitleBase):
    id: int

    class Config:
        orm_mode = True
    
class PersonBase(BaseModel):
    person_id: int
    title_id: int
    name: str
    character: Union[str, None] = None
    role: str

class Person(PersonBase):
    id: int

    class Config:
        orm_mode = True