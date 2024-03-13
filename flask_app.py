from flask import Flask, render_template

from flask_bootstrap import Bootstrap
from flask_moment import Moment

from dotenv import load_dotenv

from consts.templates import Templates

from blueprints.api import bp_api
from blueprints.app import bp_app
from blueprints.errors import bp_err

import os


env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(env_path)

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

bootstrap = Bootstrap(app)
moment = Moment(app)


@app.context_processor
def inject_constants():
    return dict(Templates=Templates)


blueprints = [bp_api, bp_app, bp_err]

for bp in blueprints:
    app.register_blueprint(bp)
