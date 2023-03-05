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
