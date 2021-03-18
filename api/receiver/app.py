from flask import Flask

from receiver.restplus import blueprint as info_blueprint


def create_receiver_app():
    app = Flask(__name__)
    app.register_blueprint(info_blueprint)
    return app


if __name__ == '__main__':
    app = create_receiver_app()
    app.run(port=5050)