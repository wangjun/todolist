from .meta import Resource
from sqlalchemy import (
    Column,
    Unicode,
)
from todolist import utils
from todolist.db import Base


class User(Resource, Base):
    __tablename__ = 'users'
    name = Column(Unicode, nullable=False)
    email = Column(Unicode, unique=True, nullable=False, index=True)
    password = Column(Unicode, nullable=False)

    def dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'created_at': utils.get_iso_format(self.created_at),
        }
