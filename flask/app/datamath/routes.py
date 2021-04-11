from . import blueprint
from flask import render_template
from Dashapps.math import *
from flask_security import login_required, roles_accepted


@blueprint.route('/pi')
# @login_required
def app4_template():
    return render_template('app4.html', dash_url = Dash_App4.url_base)

@blueprint.route('/overview')
# @login_required
def math_card_template():
    return render_template('math_cards.html')