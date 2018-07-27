from flask import Flask

#__name__ = name of module
app = Flask(__name__)

from app import routes

