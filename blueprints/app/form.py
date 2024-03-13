from flask import Blueprint, Flask, request, render_template

from datetime import datetime
from pytz import utc

from consts.templates import Templates
from forms.user import UserForm


bp = Blueprint("form", __name__)


@bp.route("/form", methods=["GET", "POST"])
def form():
    form = UserForm()

    nome = None
    sobrenome = None
    instituicao = None
    disciplina = None

    remote_addr = request.remote_addr
    remote_host = request.host

    if form.validate_on_submit():
        nome = form.nome.data
        sobrenome = form.sobrenome.data
        instituicao = form.instituicao.data
        disciplina = form.disciplina.data
        form.nome.data = None
        form.sobrenome.data = None
        form.instituicao.data = None
        form.disciplina.data = None

    return render_template(
        Templates.App.FORM.value,
        form=form,
        nome=nome,
        sobrenome=sobrenome,
        instituicao=instituicao,
        disciplina=disciplina,
        remote_addr=remote_addr,
        remote_host=remote_host,
        current_time=datetime.now(utc),
    )
