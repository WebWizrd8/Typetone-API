from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from databases import Database
from database.config import settings
from models.urlcode import metadata

DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL)
if not database_exists(engine.url):
    create_database(engine.url)

metadata.create_all(engine)

typetonedb = Database(DATABASE_URL)