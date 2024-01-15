from sqlalchemy import insert, select
from app.database.database import typetonedb
from app.models.urlcode import urlcodetable
from app.utils.shortcode import validate_code
from datetime import datetime

async def create_code_for_url(urllink: str, code: str):
    if validate_code(code) == False:
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
            return 201
    except Exception as e:
        print("ERROR message", e)
        if str(e).endswith("exists."):
            return 409

async def get_url_for_code(code: str):
    query = select(urlcodetable.c.url).where(urlcodetable.c.shortcode == code)
    return await typetonedb.fetch_one(query)

async def get_url_status_for_code(code: str):
    query = select([urlcodetable.c.created, urlcodetable.c.lastRedirect, urlcodetable.c.redirectCount]).where(urlcodetable.c.shortcode == code)

    result = await typetonedb.fetch_one(query)
    return result