from . import blueprint
from flask import render_template
from Dashapps import Dash_App8
from flask_security import login_required, roles_accepted


@blueprint.route('/corona-deaths-per-week-in-2020')
# @login_required
def app8_template():
    return render_template('app8.html', dash_url = Dash_App8.url_base)


@blueprint.route('/overview')
# @login_required
def world_card_template():
    return render_template('world_cards.html')


