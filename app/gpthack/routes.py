from flask import Blueprint, request

from chatgpt.gepeto import create_gpthack

# Create a Blueprint instance for the routes
bp = Blueprint('gpthack_routes', __name__)

@bp.route('/hack/<path:path>', methods=['GET'])
def api_get(path):
    aaa = create_gpthack()
    return f"<p>hack: {path}</p>"

