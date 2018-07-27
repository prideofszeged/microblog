from flask import Flask
from config import Config

#__name__ = name of module
app = Flask(__name__)
app.config.from_object(Config)

from app import routes
