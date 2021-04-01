from flask import Blueprint

blueprint = Blueprint(
    'finance_blueprint',
    __name__,
    url_prefix='/finance',
    template_folder='templates',
    static_folder='static'
)
