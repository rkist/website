from flask import Blueprint, request

from chatgpt.gepeto import Gepeto

# Create a Blueprint instance for the routes
bp = Blueprint('gpthack_routes', __name__)

gepeto = Gepeto()

gpthack_routes_prefix = "/hack"

def fix_pathes(html: str):
    html = html.replace("href=\"/", "href=\"/hack/")
    return html

@bp.route('/hack/<path:path>', methods=['GET'])
def api_get(path):
    print(f"Path: {path}")
    html = fix_pathes(gepeto.get_response(path))
    return html

