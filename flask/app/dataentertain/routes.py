from . import blueprint
from flask import render_template
from Dashapps.entertain import Dash_App6
from flask_security import login_required, roles_accepted


@blueprint.route('/violence-in-james-bond-movies')
# @login_required
def app6_template():
    return render_template('app6.html', dash_url = Dash_App6.url_base)

@blueprint.route('/overview')
# @login_required
def entertain_card_template():
    return render_template('entertain_cards.html')