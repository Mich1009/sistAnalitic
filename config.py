import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configuración de logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE = os.getenv("LOG_FILE", "app.log")
    
    # Configuración de caché
    CACHE_TYPE = os.getenv("CACHE_TYPE", "simple")
    CACHE_DEFAULT_TIMEOUT = 300
    
    # Configuración de sesión
    SESSION_TIMEOUT = 1800  # 30 minutos
    PERMANENT_SESSION_LIFETIME = 1800


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT', '5432')}/{os.getenv('DB_NAME')}"
    )
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    SECRET_KEY = os.getenv("PROD_SECRET_KEY", "fallback_prod_secret")
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{os.getenv('PROD_DB_USER')}:{os.getenv('PROD_DB_PASSWORD')}"
        f"@{os.getenv('PROD_DB_HOST')}:{os.getenv('PROD_DB_PORT', '5432')}/{os.getenv('PROD_DB_NAME')}"
    )
    DEBUG = False
    TESTING = False
    
    # Caché en producción
    CACHE_TYPE = "redis"
    CACHE_REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URL", "sqlite:///test.db")
    WTF_CSRF_ENABLED = False


config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}