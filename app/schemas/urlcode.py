from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CreateCodeRequest(BaseModel):
    url: Optional[str]
    shortcode: Optional[str]

class CreateCodeResponse(BaseModel):
    shortcode: str

class GetUrlforCodeResponse(BaseModel):
    url: str

class GetUrlStatusResponse(BaseModel):
    created: datetime
    lastRedirect: Optional[datetime]
    redirectCount: int