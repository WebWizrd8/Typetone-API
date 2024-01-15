from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.urlcode import (
    CreateCodeRequest,
    CreateCodeResponse,
    GetUrlforCodeResponse,
    GetUrlStatusResponse
)
from app.services import (
    create_code_for_url,
    get_for_code
)
from app.utils.shortcode import create_random_code
from app.database.database import SessionLocal, engine
from app.models.urlcode import Base

router = APIRouter()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post(
    path = "/shorten",
    status_code = 201,
    response_model=CreateCodeResponse
)
def create_shorten_code(payload: CreateCodeRequest, db: Session = Depends(get_db)) -> CreateCodeResponse:
    urlcode = payload.shortcode if payload.shortcode != None else create_random_code(6)
    result = create_code_for_url(database = db, urllink = payload.url, code = urlcode)

    if result == 409:
        raise HTTPException(status_code = 409, detail = "Shortcode already in use.")
    elif result == 412:
        raise HTTPException(status_code = 412, detail = "The provided shortcode is invalid.")

    return CreateCodeResponse (shortcode = result.shortcode)

@router.get(
    path = "/{shortcode}",
    status_code = 302,
    response_model = GetUrlforCodeResponse
)
def get_url(shortcode: str, db: Session = Depends(get_db)) -> GetUrlforCodeResponse:
    result = get_for_code(database = db, code = shortcode)

    if result == None:
        raise HTTPException(status_code = 404, detail = "Shortcode not found.")

    return GetUrlforCodeResponse (url = result.url)

@router.get(
    path = "/{shortcode}/stats",
    status_code = 200,
    response_model = GetUrlStatusResponse
)
def get_url_status(shortcode: str, db: Session = Depends(get_db)) -> GetUrlStatusResponse:
    result = get_for_code(database = db, code = shortcode)
    if result == None:
        raise HTTPException(status_code = 404, detail = "Shortcode not found")
    return GetUrlStatusResponse (created = result.created, lastRedirect = result.lastRedirect, redirectCount = result.redirectCount)