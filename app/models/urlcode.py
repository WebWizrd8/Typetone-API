from sqlalchemy import Column, Integer, String, DateTime
from app.database.database import Base

class UrlCode(Base):
    __tablename__ = "UrlCode"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    url = Column(String(), nullable = False)
    shortcode = Column(String(6), nullable = False, unique = True)
    created = Column(DateTime)
    lastRedirect = Column(DateTime)
    redirectCount = Column(Integer)