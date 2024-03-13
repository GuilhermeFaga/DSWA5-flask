from flask import Blueprint

from .update_server import bp as update_server_bp


blueprints = [update_server_bp]

bp_api = Blueprint("api", __name__, url_prefix="/api")

for bp in blueprints:
    bp_api.register_blueprint(bp)
