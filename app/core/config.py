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

    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int
    REDIS_PASSWORD: str | None

    OTP_EXPIRY_SECONDS: int

    class Config:
        env_file = ".env"


settings = Settings()