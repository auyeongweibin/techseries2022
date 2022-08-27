from flask_restful import Resource
from flask import Flask, request, jsonify

class Policies(Resource):

    def get(self):

        return {"Message": "Please use post method instead."}, 200

    def post(self):
        # json_data = request.get_json(force=True)

        return {"Message": "Here are your recommended policies"}, 200
