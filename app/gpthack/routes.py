from flask import Blueprint, request

from chatgpt.gepeto import create_gpthack

# Create a Blueprint instance for the routes
bp = Blueprint('gpthack_routes', __name__)

gpthack_routes_prefix = "/hack"

def fix_pathes(html: str):
    html = html.replace("href=\"/", "href=\"/hack/")
    return html

@bp.route('/hack/<path:path>', methods=['GET'])
def api_get(path):
    print(f"Path: {path}")
    html = fix_pathes(create_gpthack(path))
    return html

