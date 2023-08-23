from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .functions import query_chatgpt

router = APIRouter(
    prefix="/query",
    tags=["query"]
)

@router.get("/", response_model=str)
def get_recipe(
    recipe_name: str
):

    result = query_chatgpt(dish_name)

    return result