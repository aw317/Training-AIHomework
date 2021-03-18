from flask import Blueprint
from flask_restplus import Api

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)
root_blueprint = Blueprint('root', __name__)


@root_blueprint.route('/health')
def health():
    return {'message': 'Healthy'}


from ping.endpoints.ping import api as ping_api

api.add_namespace(ping_api)
