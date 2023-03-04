from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Title(Base):
    __tablename__ = 'titles'

    id = Column(Integer, primary_key=True,  autoincrement=True, nullable=True)
    title = Column(String, unique=True)
    type = Column(String)
    description = Column(String)
    release_year = Column(Integer)
    runtime = Column(Integer)

# class Person(Base):
#     __tablename__ = "credits"

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     title_id = Column(Integer, ForeignKey("title.id"))
