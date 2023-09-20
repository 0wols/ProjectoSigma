from pydantic import BaseSettings


class Settings(BaseSettings):
    # DB
    postgres_user: str
    postgres_password: str
    postgres_db: str
    database_url: str

    # AUTH
    secret_key: str
    algorithm = "HS256"
    refresh_token_expire_days = 7
    access_token_expire_minutes = 30

    # ADMIN SUPERUSER
    admin_user: str
    admin_pass: str

    class Config:
        env_file = ".env"


settings = Settings()
