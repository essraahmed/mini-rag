from pydantic_settings import BaseSettings, SettingsConfigDict

class settings(BaseSettings):

    APP_Name: str
    APP_Version: str
    OpenAI_API_Key: str
    FILE

    class Config:
        env_file = '.env'

def get_settings():
    return settings()

