from flask import Blueprint, render_template

from .index import bp as index_bp
from .contextorequisicao import bp as contextorequisicao_bp
from .user import bp as user_bp


blueprints = [
    index_bp,
    contextorequisicao_bp,
    user_bp
]

bp_app = Blueprint('app', __name__)

for bp in blueprints:
    bp_app.register_blueprint(bp)
