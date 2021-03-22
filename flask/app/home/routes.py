from . import blueprint
from flask import render_template, flash


@blueprint.route('/')
def index():
    flash('Important: Note, this site is still in preview!', 'warning')
    return render_template('index.html')