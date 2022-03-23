from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from .config import Config


app = Flask(__name__)
db=SQLAlchemy(app)
app.config.from_object(Config)
csrf=CSRFProtect
migrate=Migrate(app,db)

from app import views
from app import models