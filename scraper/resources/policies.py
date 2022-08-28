from flask_restful import Resource
from flask import Flask, request, jsonify
from application import policies_db

class Policies(Resource):

    def get(self):
        
        return {"Message": "Please use post method instead."}, 200

    def post(self):
        json_data = request.get_json(force=True)
        
        response = policies_db.scan()
        data = response['Items']

        while 'LastEvaluatedKey' in response:
            response = policies_db.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            data.extend(response['Items'])

        
        return {"Policies": data}, 200
