from pydantic_settings import BaseSettings, SettingsConfigDict

class settings (BaseSettings):
    APP_Version: str
    APP_Name: str
    OPENAI_API_KEY: str
    FILE_ALLOWED_EXTENSIONS: list[str]
    FILE_MAX_SIZE: int

    model_config = SettingsConfigDict(env_file=".env")
    # class config:
    #     env_file=".env"

def get_settings() -> settings:
    return settings()