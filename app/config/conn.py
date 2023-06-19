import psycopg2
from app.config.config import POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB, POSTGRES_SERVER, REDIS_HOST, REDIS_PORT, REDIS_PASSWORD
import redis

conn = psycopg2.connect(
    host=POSTGRES_SERVER,
    database=POSTGRES_DB,
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD
)

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)


