from flask import Blueprint

blueprint = Blueprint(
    'entertain_blueprint',
    __name__,
    url_prefix='/entertainment',
    template_folder='templates',
    static_folder='static'
)
