import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Import Migrate

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Initialize Migrate

from datevault import routes  # noqa