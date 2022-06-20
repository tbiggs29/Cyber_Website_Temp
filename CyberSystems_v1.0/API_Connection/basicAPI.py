from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)


class PGN(Resource):
    def get(self, PGN):
        with open("J1939.json", "r") as jsonFile:
            data = json.load(jsonFile) 
        return {"PGN": {PGN: data["PGN"][PGN]}}

class SPN(Resource):
    def get(self, SPN):
        with open("J1939.json", "r") as jsonFile:
            data = json.load(jsonFile) 
        return {"SPN": {SPN : data["SPN"][SPN]}}

class SA(Resource):
    def get(self, SA):
        with open("J1939.json", "r") as jsonFile:
            data = json.load(jsonFile) 
        return {"SA": {SA: data["SA"][SA]}}
    

class FMI(Resource):
    def get(self, SPN):
        with open("J1939.json", "r") as jsonFile:
            data = json.load(jsonFile) 
        return data["PGN"][PGN]

class SLOT(Resource):
    def get(self, SPN):
        with open("J1939.json", "r") as jsonFile:
            data = json.load(jsonFile) 
        return data["PGN"][PGN]

api.add_resource(PGN, '/PGN/<PGN>')
api.add_resource(SPN, '/SPN/<SPN>')
api.add_resource(SA, '/SA/<SA>')

if __name__ == '__main__':
    app.run(debug=False)