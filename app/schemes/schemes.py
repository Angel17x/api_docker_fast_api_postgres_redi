from databases import Database
import sqlalchemy
from app.config.config import DATABASE_URL;
import psycopg2

database = Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

user = sqlalchemy.Table(
    "user",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("lastname", sqlalchemy.String),
    sqlalchemy.Column("age", sqlalchemy.Integer),
    sqlalchemy.Column("nickname", sqlalchemy.String),
    sqlalchemy.Column("password", sqlalchemy.String),
    sqlalchemy.Column("work", sqlalchemy.String),
)


engine = sqlalchemy.create_engine(str(database.url))

metadata.create_all(engine)