from flask import Blueprint, Flask, redirect, request, render_template, session, url_for

from datetime import datetime
from pytz import utc

from consts.templates import Templates
from forms.login import LoginForm


bp = Blueprint("login", __name__)


@bp.route("/login", methods=["GET", "POST"])
def form():
    form = LoginForm()

    remote_addr = request.remote_addr
    remote_host = request.host

    if form.validate_on_submit():
        session["username"] = form.username.data
        session["password"] = form.username.data
        session["remote_addr"] = request.remote_addr
        session["host"] = request.host
        return redirect(url_for("app.index.index"))

    return render_template(
        Templates.App.LOGIN.value,
        form=form,
        remote_addr=remote_addr,
        remote_host=remote_host,
        current_time=datetime.now(utc),
    )
