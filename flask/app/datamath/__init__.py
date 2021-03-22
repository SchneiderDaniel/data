from flask import Blueprint

blueprint = Blueprint(
    'math_blueprint',
    __name__,
    url_prefix='/math',
    template_folder='templates',
    static_folder='static'
)
