from . import blueprint
from flask import render_template
from Dashapps import Dash_App5
from flask_security import login_required, roles_accepted


@blueprint.route('/bitcoin')
# @login_required
def app5_template():
    return render_template('app5.html', dash_url = Dash_App5.url_base)

@blueprint.route('/overview')
# @login_required
def crypto_card_template():
    return render_template('crypto_cards.html')