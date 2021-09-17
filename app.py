# Flask web server
from flask import Flask
from flask_restful import Resource, Api

from server_util import *

app = Flask(__name__)
api = Api(app)


class SubQuery(Resource):
    def get(self):
        return {
            "Hello": "World"
        }


if __name__ == '__main__':
    app.run()
