from flask_restful import Resource
from flask import Flask, request, jsonify
from application import client

class Policies(Resource):

    def get(self):
        # client.create_table(
        #     AttributeDefinitions = [ # Name and type of the attributes 
        #         {
        #             'AttributeName': 'Company', # Name of the attribute
        #             'AttributeType': 'S'   # N -> Number (S -> String, B-> Binary)
        #         },
        #         {
        #             'AttributeName': 'Policy Name', # Name of the attribute
        #             'AttributeType': 'S'   # N -> Number (S -> String, B-> Binary)
        #         },
        #         {
        #             'AttributeName': 'Premium Type', # Name of the attribute
        #             'AttributeType': 'S'   # N -> Number (S -> String, B-> Binary)
        #         },
        #         {
        #             'AttributeName': 'Product Summary', # Name of the attribute
        #             'AttributeType': 'S'   # N -> Number (S -> String, B-> Binary)
        #         },
        #         {
        #             'AttributeName': 'Features', # Name of the attribute
        #             'AttributeType': 'S'   # N -> Number (S -> String, B-> Binary)
        #         }
        #     ],
        #     TableName = 'Policies', # Name of the table 
        #     KeySchema = [       # Partition key/sort key attribute 
        #         {
        #             'AttributeName': 'Policy Name',
        #             'KeyType'      : 'HASH' 
        #             # 'HASH' -> partition key, 'RANGE' -> sort key
        #         }
        #     ],
        #     BillingMode = 'PAY_PER_REQUEST',
        #     Tags = [ # OPTIONAL 
        #         {
        #             'Key' : 'test-resource',
        #             'Value': 'dynamodb-test'
        #         }
        #     ]
        # )

        return {"Message": "Please use post method instead."}, 200

    def post(self):
        # json_data = request.get_json(force=True)
        policies = [
            {
                "Company": "AIA Singapore",
                "Policy Name": "AIA Elite Secure Income (10 Pay)",
                "Premium Type": "Annual Premium",
                "Product Summary": "https://www.comparefirst.sg/wap/prodSummaryPdf/201106386R/WA_Sum_201106386R_ESI10P_Jan2022.pdf",
                "Features": [
                    False,
                    True,
                    False,
                    False,
                    True
                ]
            },
            {
                "Company": "AIA Singapore",
                "Policy Name": "AIA Elite Secure Income (5 Pay)",
                "Premium Type": "Annual Premium",
                "Product Summary": "https://www.comparefirst.sg/wap/prodSummaryPdf/201106386R/WA_Sum_201106386R_ESI5P_Jan2022.pdf",
                "Features": [
                    False,
                    True,
                    False,
                    False,
                    True
                ]
            },
            {
                "Company": "AIA Singapore",
                "Policy Name": "AIA Elite Secure Income (Single Pay)",
                "Premium Type": "Single Premium",
                "Product Summary": "https://www.comparefirst.sg/wap/prodSummaryPdf/201106386R/WA_Sum_201106386R_ESISP_Jan2022.pdf",
                "Features": [
                    False,
                    True,
                    True,
                    False,
                    True
                ]
            },
        ]


        
        return {"Policies": policies}, 200
