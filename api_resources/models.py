from flask_restful_swagger_2 import Schema


class ErrorModel(Schema):
    type = 'object'
    properties = {
        'message': {
            'type': 'string'
        }
    }


class ResponseModel(Schema):
    type = 'object'
    properties = {
        'message': {
            'type': 'string'
        }
    }