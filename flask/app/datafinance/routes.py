from . import blueprint
from flask import render_template
from Dashapps.finance import *
from flask_security import login_required, roles_accepted


@blueprint.route('/rebalancing')
# @login_required
def app1_template():
    return render_template('app1.html', dash_url = Dash_App1.url_base, meta_text=Dash_App1.description_text)

@blueprint.route('/correlation')
# @login_required
# @roles_accepted('admin')
def app2_template():
    return render_template('app2.html', dash_url = Dash_App2.url_base, meta_text=Dash_App2.description_text)


@blueprint.route('/impact-of-fond-costs')
@login_required
@roles_accepted('admin')
def app3_template():
    return render_template('app3.html', dash_url = Dash_App3.url_base, meta_text=Dash_App3.description_text)


@blueprint.route('/overview')
# @login_required
def finance_card_template():
    return render_template('finance_cards.html')