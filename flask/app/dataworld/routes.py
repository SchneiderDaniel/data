from . import blueprint
from flask import render_template
from Dashapps.world import *
from flask_security import login_required, roles_accepted


@blueprint.route('/corona-deaths-per-week-in-2020')
def app8_template():
    return render_template('app8.html', dash_url = Dash_App8.url_base)

@blueprint.route('/how-happy-are-people-in-each-country')
def app9_template():
    return render_template('app9.html', dash_url = Dash_App9.url_base)

@blueprint.route('/what-is-the-worldwide-life-expectancy')
def app10_template():
    return render_template('app10.html', dash_url = Dash_App10.url_base)


@blueprint.route('/overview')
def world_card_template():
    return render_template('world_cards.html')


