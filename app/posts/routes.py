from flask import Blueprint, request

from posts.post import create_post, list_posts

# Create a Blueprint instance for the routes
bp = Blueprint('post_routes', __name__)

@bp.route('/post', methods=['POST'])
def api_post():
    data = request.get_json()
    return create_post(data)

@bp.route('/post', methods=['GET'])
def api_get():
    return list_posts()

@bp.route('/post', methods=['PUT'])
def api_put():
    #TODO
    return 'TODO: api put'

@bp.route('/post', methods=['DELETE'])
def api_delete():
    #TODO
    return 'TODO: api delete'