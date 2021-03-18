from flask_restplus import Namespace

from flask_restplus import Resource

api = Namespace('info', description='Url info providing operations')


@api.route('')
class Receiver(Resource):

    @api.doc('Return hardcoded json')
    def get(self):
        '''Return hardcoded json'''

        return {"Receiver": "Cisco is the best!"}
