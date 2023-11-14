from sqlalchemy import Column, Integer, ForeignKey, DATETIME, TEXT, String, Boolean, Date, DateTime
from sqlalchemy.orm import relationship

from database.database import Base
from enum import Enum

class User(Base):

    __tablename__ = "user"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)

    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String)

    last_connection = Column(DateTime)
    registration_date = Column(Date, nullable=False)

    enabled = Column(Boolean, default=True, nullable=False)