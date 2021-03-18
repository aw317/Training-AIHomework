from flask import Flask

from ping.restplus import blueprint as ping_blueprint, root_blueprint


def create_ping_app():
    app = Flask(__name__)
    app.register_blueprint(ping_blueprint)
    app.register_blueprint(root_blueprint)
    return app


if __name__ == '__main__':
    app = create_ping_app()
    app.run(port=5050)
