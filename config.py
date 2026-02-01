import json
from os import getenv, path
from dotenv import load_dotenv

load_dotenv(path.realpath(".env"))


class Config:
    """Config file"""
    TESTING = getenv("TESTING")
    FLASK_DEBUG = json.loads(getenv("FLASK_DEBUG").lower())
    SECRET_KEY = getenv("SECRET_KEY")
    SERVER = getenv("SERVER")
    PORT = int(getenv("PORT"))
    RIOT_KEY = getenv("RIOT_KEY")
