from sqlalchemy.orm import Session
from datetime import date, datetime
from typing import List

from common.exceptions import Exceptions
from common.utils import get_password_hash, create_uuid

from user import schemas, models


def get_user(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_user(db: Session, user: schemas.UserCreate):

    try:

        db_user = models.User(
            id=create_uuid(),
            name=user.name,
            email=user.email,
            birth_date=user.birth_date,
            gender=user.gender,
            country=user.country,
            document_type=user.document_type,
            document_number=user.document_number,
            hashed_password=get_password_hash(user.password),
            registration_date=date.today(),
        )

    except Exception:
        raise Exceptions.user_create_exception

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def update_user(db: Session, user: schemas.UserUpdate, current_user_id: str):
    db_user = get_user(db, current_user_id)

    if not db_user:
        raise Exceptions.user_not_found_exception


def disable_user(db: Session, user_id: str):
    db_user = get_user(db, user_id)

    if not db_user:
        raise Exceptions.user_not_found_exception

    db_user.enabled = False
    db.commit()
    db.refresh(db_user)

    return db_user
