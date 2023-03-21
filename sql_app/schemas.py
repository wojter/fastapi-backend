from typing import Union, List
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


class TitleWithPeople(Title):
    people: List[Person] = []

class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None

class UserInDB(User):
    hashed_password: str