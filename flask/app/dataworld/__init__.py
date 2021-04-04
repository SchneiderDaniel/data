from flask import Blueprint

blueprint = Blueprint(
    'world_blueprint',
    __name__,
    url_prefix='/world',
    template_folder='templates',
    static_folder='static'
)
