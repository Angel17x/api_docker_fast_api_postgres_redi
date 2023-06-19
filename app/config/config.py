from starlette.config import Config
from starlette.datastructures import Secret
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'env.dev');
config = Config(dotenv_path);

PROJECT_NAME = "phresh";
VERSION = "1.0.0";
API_PREFIX = "/api";
SECRET_KEY = config("SECRET_KEY", cast=Secret, default="CHANGEME");
POSTGRES_USER = config("POSTGRES_USER", cast=str);
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=Secret);
POSTGRES_SERVER = config("POSTGRES_SERVER", cast=str, default="db");
POSTGRES_PORT = config("POSTGRES_PORT", cast=str, default="5432");
POSTGRES_DB = config("POSTGRES_DB", cast=str);
REDIS_PORT = config("REDIS_PORT", cast=str, default=6379);
REDIS_HOST = config("REDIS_HOST", cast=str, default="CHANGEME");
REDIS_USERNAME = config("REDIS_USERNAME", cast=str, default="CHANGEME");
REDIS_PASSWORD = config("REDIS_PASSWORD", cast=str, default="CHANGEME");
JWT_ALGORITHM = "HS256"
JWT_EXP_DELTA_SECONDS = 3600