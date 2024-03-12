from flask import Blueprint, render_template


bp = Blueprint('user', __name__)


@bp.route('/user/<name>/<prontuario>/<institution>')
def user(name, prontuario, institution):
    return render_template('user.html', 
                           name=name, 
                           prontuario=prontuario,
                           institution=institution);