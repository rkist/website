from flask import Blueprint, request

from posts.post import create_post, list_posts

# Create a Blueprint instance for the routes
bp = Blueprint('post_routes', __name__)

@bp.route('/')
def index():
    return 'index page!'

@bp.route('/about')
def about():
    return 'about page.'

@bp.route('/api', methods=['POST'])
def api_post():
    data = request.get_json()
    return create_post(data)

@bp.route('/api', methods=['GET'])
def api_get():
    return list_posts()

@bp.route('/api', methods=['PUT'])
def api_put():
    #TODO
    return 'TODO: api put'

@bp.route('/api', methods=['DELETE'])
def api_delete():
    #TODO
    return 'TODO: api delete'