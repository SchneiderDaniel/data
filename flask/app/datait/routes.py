from . import blueprint
from flask import render_template
from Dashapps.it import *
from flask_security import login_required, roles_accepted


@blueprint.route('/what-are-the-most-popular-programming-languages')
# @login_required
def app7_template():
    return render_template('app7.html', dash_url = Dash_App7.url_base, meta_text=Dash_App7.description_text)

@blueprint.route('/most-used-characters-in-hello-world')
# @login_required
def app15_template():
    return render_template('app15.html', dash_url = Dash_App15.url_base, meta_text=Dash_App15.description_text)


@blueprint.route('/length-of-hello-world-programs')
# @login_required
def app16_template():
    return render_template('app16.html', dash_url = Dash_App16.url_base, meta_text=Dash_App16.description_text)


@blueprint.route('/overview')
# @login_required
def it_card_template():
    return render_template('it_cards.html')