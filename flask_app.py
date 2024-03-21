from flask import Flask, session

from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_migrate import Migrate

from sqlalchemy import URL

from dotenv import load_dotenv

from consts.templates import Templates

from blueprints.api import bp_api
from blueprints.app import bp_app
from blueprints.errors import bp_err

from ext.database import db

from models.user import User
from models.role import Role

import os


env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(env_path)

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY") or "you-will-never-guess"

bootstrap = Bootstrap(app)
moment = Moment(app)
migration = Migrate(app, db)

# connection_string = URL.create(
#     "postgresql",
#     username=os.environ.get("SQLALCHEMY_USER"),
#     password=os.environ.get("SQLALCHEMY_PASSWORD"),
#     host=os.environ.get("SQLALCHEMY_HOST"),
#     database=os.environ.get("SQLALCHEMY_DATABASE"),
# )

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.context_processor
def inject_constants():
    return dict(Templates=Templates, session=session)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)


blueprints = [bp_api, bp_app, bp_err]

for bp in blueprints:
    app.register_blueprint(bp)
