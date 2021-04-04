from flask import Blueprint

blueprint = Blueprint(
    'crypto_blueprint',
    __name__,
    url_prefix='/cryptocurrency',
    template_folder='templates',
    static_folder='static'
)
