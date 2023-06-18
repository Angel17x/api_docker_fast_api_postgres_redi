from fastapi import FastAPI
from app.routes.routes import router
from app.config.config import DATABASE_URL
import logging
from databases import Database

logger = logging.getLogger(__name__)


app = FastAPI()


app.include_router(router)
