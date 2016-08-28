
from flask import render_template, Blueprint, redirect, url_for
# from flask_login import login_required


api_blueprint = Blueprint('api', __name__)


@api_blueprint.route("/")
# @login_required
def index():
    # return redirect(url_for('dashboard.get_dashboard'))
    return "hello world";

