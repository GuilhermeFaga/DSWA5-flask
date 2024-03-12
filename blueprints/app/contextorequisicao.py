from flask import Blueprint, request, render_template

from consts.templates import Templates


bp = Blueprint('contextorequisicao', __name__)


@bp.route('/contextorequisicao/<name>')
def contextorequisicao(name):
    user_agent = request.headers.get('User-Agent');
    remote_addr = request.remote_addr;
    remote_host = request.host;
    return render_template(Templates.App.CONTEXTO.value,
                           name=name, 
                           user_agent=user_agent, 
                           remote_addr=remote_addr,
                           remote_host=remote_host);