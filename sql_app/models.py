from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Titles(Base):
    __tablename__ = 'titles'

    id = Column(Integer, primary_key=True,  autoincrement=True)
    title = Column(String, unique=True)
    type = Column(String)
    description = Column(String)
    release_year = Column(Integer)
    runtime = Column(Integer)


class Person(Base):
    __tablename__ = "credits"

    id = Column(Integer, primary_key=True,  autoincrement=True)
    person_id = Column(Integer)
    title_id = Column(Integer, ForeignKey("titles.id"))
    name = Column(String)
    character = Column(String)
    role = Column(String)
