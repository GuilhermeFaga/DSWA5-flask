from flask import Blueprint, render_template, redirect, url_for, session

from consts.templates import Templates

from forms.username import UsernameForm

from ext.database import db
from models.user import User

from datetime import datetime
from pytz import utc


bp = Blueprint("index", __name__)


@bp.route("/", methods=["GET", "POST"])
def index():
    form = UsernameForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        print(User.get_by_username(form.username.data))
        if User.get_by_username(form.username.data) is None:
            user = User(username=form.username.data)
            db.session.add(user)
            db.session.commit()
            session["known"] = False
        else:
            session["known"] = True

        session["username"] = form.username.data
        return redirect(url_for("app.index.index"))

    return render_template(Templates.App.INDEX.value, form=form)
