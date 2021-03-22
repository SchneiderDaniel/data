from . import blueprint
from flask import render_template
from Dashapps import Dash_App4
from flask_security import login_required, roles_accepted


@blueprint.route('/pi')
# @login_required
def app4_template():
    return render_template('app4.html', dash_url = Dash_App4.url_base)

