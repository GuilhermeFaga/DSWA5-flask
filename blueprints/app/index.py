from flask import Blueprint, render_template, session

from consts.templates import Templates

from datetime import datetime
from pytz import utc


bp = Blueprint("index", __name__)


@bp.route("/")
def index():
    return render_template(
        Templates.App.INDEX.value,
        current_time=datetime.now(utc),
        username=session.get("username"),
    )
