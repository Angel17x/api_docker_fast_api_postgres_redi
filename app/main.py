from fastapi import FastAPI
from app.routes.routes import router
import logging
from app.config.conn import conn
from fastapi.middleware.cors import CORSMiddleware
logger = logging.getLogger(__name__)


origins = ["*"]
app = FastAPI()

app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.middleware("http")

# @AuthJWT.load_config