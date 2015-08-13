from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    DateTime,
)


class Resource(object):
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow())
