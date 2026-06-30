from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str

    REDIS_HOST: str
    REDIS_PORT: int

    SECRET_KEY: str
    ALGORITHM: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYS: int

    SMTP_EMAIL: str
    SMTP_PASSWORD: str

    class Config:
        env_file = ".env"


settings = Settings()