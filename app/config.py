import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings():
    
    DB_USER: str = os.getenv('DB_USER')
    DB_NAME: str = os.getenv('DB_NAME')
    DB_PASSWORD: str = os.getenv('DB_PASSWORD')
    DB_HOST: str = os.getenv('DB_HOST')
    DB_HOSTNAME: str = os.getenv('DB_HOSTNAME')
    DB_PORT: str = os.getenv('DB_PORT')
    DB_URL: str = os.getenv('DB_URL')
    

settings = Settings()
