from . import blueprint
from flask import render_template
from Dashapps.entertain import *
from flask_security import login_required, roles_accepted


@blueprint.route('/violence-in-james-bond-movies')
# @login_required
def app6_template():
    return render_template('app6.html', dash_url = Dash_App6.url_base, meta_text=Dash_App6.description_text)

@blueprint.route('/return-of-disney-movies')
# @login_required
def app17_template():
    return render_template('app17.html', dash_url = Dash_App17.url_base, meta_text=Dash_App17.description_text)

@blueprint.route('/overview')
# @login_required
def entertain_card_template():
    return render_template('entertain_cards.html')