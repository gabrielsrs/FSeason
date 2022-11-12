from os import getenv, path
from dotenv import load_dotenv

load_dotenv(path.realpath(".env"))


class Config:
    """Config file"""
    TESTING = getenv("TESTING")
    FLASK_DEBUG = getenv("FLASK_DEBUG")
    SECRET_KEY = getenv("SECRET_KEY")
    SERVER = getenv("SERVER")
    PORT = getenv("PORT")
    RIOT_KEY = getenv("RIOT_KEY")


