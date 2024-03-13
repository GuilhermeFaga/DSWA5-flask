from flask import Blueprint, render_template


from consts.templates import Templates

bp_err = Blueprint("errors", __name__)


@bp_err.app_errorhandler(404)
def not_found(e):
    return render_template(Templates.Errors.NOT_FOUND.value), 404


@bp_err.app_errorhandler(500)
def server_error(e):
    return render_template(Templates.Errors.SERVER_ERROR.value), 500
