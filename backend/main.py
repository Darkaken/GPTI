
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.database import engine, Base

from router import Router, add_routers

origins = [
    "http://localhost",
    "http://localhost:8080",
    "*",
]

Base.metadata.create_all(bind=engine)

app = FastAPI()

router = Router()
router = add_routers(router)
app = router.include(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)