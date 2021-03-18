from flask import Blueprint
from flask_restplus import Api

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)

from receiver.endpoints.info import api as info_api

api.add_namespace(info_api)
