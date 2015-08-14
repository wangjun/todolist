from .meta import Resource
from sqlalchemy import (
    Column,
    Unicode,
)
from todolist.db import Base

class User(Resource, Base):
    __tablename__ = 'users'
    name = Column(Unicode, nullable=False)
    email = Column(Unicode, unique=True, nullable=False, index=True)
    password = Column(Unicode, nullable=False)
