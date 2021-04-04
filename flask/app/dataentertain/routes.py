from . import blueprint
from flask import render_template
from Dashapps import Dash_App6
from flask_security import login_required, roles_accepted


@blueprint.route('/gameofthrones')
# @login_required
def app6_template():
    return render_template('app6.html', dash_url = Dash_App6.url_base)
