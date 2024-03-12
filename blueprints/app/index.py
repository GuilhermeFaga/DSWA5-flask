from flask import Blueprint, render_template

from datetime import datetime


bp = Blueprint('index', __name__)


@bp.route('/')
def index():
     return render_template('index.html', current_time=datetime.utcnow())
