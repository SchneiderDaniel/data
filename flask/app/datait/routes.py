from . import blueprint
from flask import render_template
from Dashapps import Dash_App7
from flask_security import login_required, roles_accepted


@blueprint.route('/success-of-ai-projects')
# @login_required
def app7_template():
    return render_template('app7.html', dash_url = Dash_App7.url_base)

@blueprint.route('/overview')
# @login_required
def it_card_template():
    return render_template('it_cards.html')