from typing import Annotated
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.database import engine, Base

from query.endpoints import router as queryRouter

origins = [
    "http://localhost",
    "http://localhost:8080",
    "*",
]

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(queryRouter)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)