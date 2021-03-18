import requests
from flask import jsonify
from flask_restplus import Namespace
from flask_restplus import Resource

from ping.serializers import ping_json

api = Namespace('ping', description='Ping related operations')


@api.route('')
class Ping(Resource):

    @api.doc('Ping given url')
    @api.expect(ping_json, validate=True)
    def post(self):
        '''Ping given url'''

        try:
            return jsonify(requests.get(api.payload['url'], verify=False).json())
        except Exception as ex:
            return requests.get(api.payload['url'], verify=False).text
