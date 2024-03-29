from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)
from zope.sqlalchemy import ZopeTransactionExtension
from sqlalchemy.ext.declarative import declarative_base


session = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()
