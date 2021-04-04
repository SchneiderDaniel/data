from flask import Blueprint

blueprint = Blueprint(
    'it_blueprint',
    __name__,
    url_prefix='/computerscience',
    template_folder='templates',
    static_folder='static'
)
