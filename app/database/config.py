from pydantic import BaseSettings, Field

class Config(BaseSettings):
    DATABASE_URL: str = Field("", env="DATABASE_URL")
    
    class Config:
        env_prefix = ""
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Config()