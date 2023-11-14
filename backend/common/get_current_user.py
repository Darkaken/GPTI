from typing import Annotated
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from jose import JWTError, jwt

from config import Settings, get_settings
from database.dependencies import get_db

from .exceptions import Exceptions

from user.schemas import UserOut
from user.functionality.crud import get_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    settings: Annotated[Settings, Depends(get_settings)],
    db: Annotated[Session, Depends(get_db)]
):

    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])

        user_id: str = payload.get("user_id")

        if user_id is None:
            raise Exceptions.credentials_exception

    except JWTError:
        raise Exceptions.credentials_exception

    user = get_user(db, user_id)

    if user is None:
        raise Exceptions.credentials_exception

    return UserOut(**user.__dict__())



