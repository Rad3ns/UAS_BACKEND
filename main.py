
from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS
import json
app = Flask(__name__)
api = Api(app)
CORS(app)
version = "v1"


class Home(Resource):
    def get(self):
        home = open("home.json", "r")
        jsonHome = json.load(home)
        return {"home": jsonHome}


api.add_resource(Home, f'/{version}/home/')


if __name__ == '__main__':
    app.run()
