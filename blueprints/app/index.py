from flask import Blueprint, render_template

from consts.templates import Templates

from datetime import datetime


bp = Blueprint("index", __name__)


@bp.route("/")
def index():
    return render_template(Templates.App.INDEX.value, current_time=datetime.utcnow())
