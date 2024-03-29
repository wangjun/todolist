from datetime import datetime
from todolist import db
from sqlalchemy import (
    Column,
    Integer,
    DateTime,
)


class Resource(object):
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow())

    @classmethod
    def query(cls):
        return db.session.query(cls)

    def save(self):
        db.session.add(self)
        db.session.flush()

    def delete(self):
        db.session.delete(self)
