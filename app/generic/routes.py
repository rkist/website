from flask import Blueprint, request

# Create a Blueprint instance for the routes
bp = Blueprint('generic_routes', __name__)

@bp.route('/')
def index():
    return 'index page!'

@bp.route('/about')
def about():
    return 'about page.'

