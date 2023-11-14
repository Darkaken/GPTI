from fastapi import APIRouter, Depends

from functionality.functions import query_chatgpt
from database.dependencies import get_db
from typing import List, Annotated
from sqlalchemy.orm import Session

from common.get_current_user import get_current_user
from user.schemas import UserOut

router = APIRouter(
    prefix="/query",
    tags=["query"]
)

@router.get("/", response_model=str)
async def get_recipe(
    db: Annotated[Session, Depends(get_db)],
    current_user: Annotated[UserOut, Depends(get_current_user)], #check if current user is a valid user
    dish_name: str
):

    result = query_chatgpt(dish_name)

    return result