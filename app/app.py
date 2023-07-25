from flask import Flask
from posts.routes import bp as routes_bp
from generic.routes import bp as generic_bp
from gpthack.routes import bp as gpthack_bp

app = Flask(__name__)

@app.route('/health')
def healthcheck():
    return "Looking good!"

if __name__== '__main__':
    app.register_blueprint(routes_bp)
    app.register_blueprint(generic_bp)
    app.register_blueprint(gpthack_bp)

    app.run(
        host="127.0.0.1",
        port="5000"
    )