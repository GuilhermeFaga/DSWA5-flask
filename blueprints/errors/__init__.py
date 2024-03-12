from flask import Blueprint, render_template


bp_err = Blueprint('errors', __name__)

@bp_err.app_errorhandler(404)
def not_found(e):
   return render_template('404.html'), 404


@bp_err.app_errorhandler(500)
def server_error(e):
   return render_template('500.html'), 500
