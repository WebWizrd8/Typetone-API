from sqlalchemy import select
from app.models.urlcode import UrlCode
from app.utils.shortcode import validate_code
from app.utils.shortcode import create_random_code
from sqlalchemy import select
from sqlalchemy.orm import Session
from datetime import datetime

def create_code_for_url(database: Session, urllink: str, code: str):
    if validate_code(code) == False:
        return 412
    
    query = select(UrlCode.id).where(UrlCode.shortcode == code)
    existCode = database.execute(query).scalars().all()
    if len(existCode) > 0:
        return 409

    new_urlcode = UrlCode(
       url = urllink,
       shortcode = code,
       created = datetime.utcnow(),
       lastRedirect = None,
       redirectCount = 0
   )
    
    database.add(new_urlcode)
    database.commit()
    database.refresh(new_urlcode)

    return new_urlcode

def get_url_for_code(database: Session, code: str):
    urlcode = database.query(UrlCode).filter(UrlCode.shortcode == code).first()
    urlcode.redirectCount += 1
    urlcode.lastRedirect = datetime.utcnow()
    database.commit()
    return urlcode

def get_stats_for_code(database: Session, code: str):
    result = database.query(UrlCode).filter(UrlCode.shortcode == code).first()
    return result