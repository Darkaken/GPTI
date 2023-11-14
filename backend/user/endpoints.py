from typing import List, Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.dependencies import get_db
from datetime import timedelta

from config import get_settings, Settings

from fastapi import APIRouter, Depends, HTTPException, status

from .schemas import UserOut, UserCreate, UserUpdate
from .functionality import crud

from common.get_current import get_current_agent
from common.utils import create_token
from common.schemas import Token

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.get("/", response_model=UserOut)
async def get_user(
    db: Annotated[Session, Depends(get_db)],
    user_id: str
):
    return crud.get_user(db, user_id)


@router.post("/", response_model=Token)
async def create_user(
    db: Annotated[Session, Depends(get_db)],
    user: UserCreate,
):
    db_user = crud.create_user(db, user)
    return create_token(db_user.id)

@router.put("/", response_model=UserUpdate)
async def update_user(
    db: Annotated[Session, Depends(get_db)],
    user: UserUpdate,
    current_user = Annotated[UserOut, Depends(get_current_agent)]
):

    return crud.update_user(db, user, current_user.id)

@router.delete("/", response_model=int)
async def disable_user(
    db: Annotated[Session, Depends(get_db)],
    user_id: str
):
    return crud.disable_user(db, user_id)
