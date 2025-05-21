from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):# S letter should be upper case or lower case it does not matter
    APP_NAME:str
    APP_VERSION:str
    GROQ_API_KEY:str
    FILE_ALLOWED_TYPES:list
    FILE_MAX_SIZE:int
    FILE_DEFAULT_CHUNK_SIZE : int
    MONGODB_URI:str
    MONGODB_DATABASE:str


    class Config:# C letter should be upper case
        env_file = ".env"
        
def get_settings():
    return Settings()