from flask import Blueprint, render_template


from consts.templates import Templates


bp = Blueprint('user', __name__)


@bp.route('/user/<name>/<prontuario>/<institution>')
def user(name, prontuario, institution):
    return render_template(Templates.App.USER.value, 
                           name=name, 
                           prontuario=prontuario,
                           institution=institution);