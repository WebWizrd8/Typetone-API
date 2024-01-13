from sqlalchemy import insert, select
from database.database import typetonedb
from models.urlcode import urlcodetable
from datetime import datetime
import re

async def create_code_for_url(urllink: str, code: str):
    if len(code) != 6 or not re.fullmatch(r'[A-Za-z0-9_]*$', code):
        return 412

    query = urlcodetable.insert().values(
        url = urllink,
        shortcode = code,
        created = datetime.utcnow(),
        lastRedirect = None,
        redirectCount = 0
    )

    try:
        result = await typetonedb.execute(query)
        if result is not None:
            return 302
    except Exception as e:
        if str(e).endswith("exists."):
            return 409

async def get_url_for_code(code: str):
    query = select(urlcodetable.c.url).where(urlcodetable.c.shortcode == code)
    return await typetonedb.fetch_one(query)

async def get_url_status_for_code(code: str):
    query = select([urlcodetable.c.created, urlcodetable.c.lastRedirect, urlcodetable.c.redirectCount]).where(urlcodetable.c.shortcode == code)

    result = await typetonedb.fetch_one(query)
    return result