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

@blueprint.route('/what-is-the-social-support-worldwide')
def app11_template():
    return render_template('app11.html', dash_url = Dash_App11.url_base)

@blueprint.route('/most-generous-people-in-the-world')
def app12_template():
    return render_template('app12.html', dash_url = Dash_App12.url_base)

@blueprint.route('/highest-freedom-for-making-life-choices-worldwide')
def app13_template():
    return render_template('app13.html', dash_url = Dash_App13.url_base)

@blueprint.route('/highest-perception-for-corruption-worldwide')
def app14_template():
    return render_template('app14.html', dash_url = Dash_App14.url_base)



####--------###

@blueprint.route('/overview')
def world_card_template():
    return render_template('world_cards.html')


