from ping.restplus import api
from flask_restplus import fields

ping_json = api.model('Ping', {'url': fields.Url(required=True, description='Url to ping',
                                                )},)
