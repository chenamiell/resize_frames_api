from flask import Flask
from flask_cors import CORS
from flask_restful_swagger_2 import Api

from api_resources.views import ResizeVideoFramesResource

app = Flask(__name__)
CORS(app)
api = Api(app, api_version='0.1')

api.add_resource(ResizeVideoFramesResource, '/video/resize_frames')


@app.route('/')
def index():
    return """<head>
    <meta http-equiv="refresh" content="0; url=http://petstore.swagger.io/?url=http://localhost:5000/api/swagger.json" />
    </head>"""


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True)
