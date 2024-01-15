from fastapi import APIRouter, HTTPException
from app.schemas.urlcode import (
    CreateCodeRequest,
    CreateCodeResponse,
    GetUrlforCodeResponse,
    GetUrlStatusResponse
)
from app.services import (
    create_code_for_url,
    get_url_for_code,
    get_url_status_for_code
)
from app.utils.shortcode import create_random_code

router = APIRouter()

@router.get(path = "/")
def helloworld():
    return {"message": "Hello, world!"}

@router.post(
    path = "/shorten",
    status_code = 201,
    response_model=CreateCodeResponse
)
async def create_shorten_code(payload: CreateCodeRequest) -> CreateCodeResponse:
    urlcode = payload.shortcode if payload.shortcode != None else create_random_code(6)
    result = await create_code_for_url(urllink = payload.url, code = urlcode)

    if result == 409:
        raise HTTPException(status_code = 409, detail = "Shortcode already in use.")
    elif result == 412:
        raise HTTPException(status_code = 412, detail = "The provided shortcode is invalid.")

    return CreateCodeResponse (shortcode = urlcode)

@router.get(
    path = "/{shortcode}",
    response_model = GetUrlforCodeResponse
)
async def get_url(shortcode: str) -> GetUrlforCodeResponse:
    result = await get_url_for_code(code = shortcode)

    if result == None:
        raise HTTPException(status_code = 404, detail = "Shortcode not found.")

    return GetUrlforCodeResponse (url = result.url)

@router.get(
    path = "/{shortcode}/stats",
    status_code = 200,
    response_model = GetUrlStatusResponse
)
async def get_url_status(shortcode: str) -> GetUrlStatusResponse:
    result = await get_url_status_for_code(code = shortcode)
    if result == None:
        raise HTTPException(status_code = 404, detail = "Shortcode not found")
    return GetUrlStatusResponse (created = result.created, lastRedirect = result.lastRedirect, redirectCount = result.redirectCount)