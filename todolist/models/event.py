from .meta import Resource
from sqlalchemy import (
    Column,
    Unicode,
    Integer,
    ForeignKey,
    DateTime,
)
from sqlalchemy.orm import relationship, backref
from todolist import utils
from todolist.db import Base


class Event(Resource, Base):
    __tablename__ = 'events'
    title = Column(Unicode, nullable=False)
    description = Column(Unicode)
    due_date = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', backref=backref('items', lazy='dynamic'))

    def dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'due_date': utils.get_iso_format(self.due_date),
            'created_at': utils.get_iso_format(self.created_at),
        }
