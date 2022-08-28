from flask_restful import Resource
from flask import Flask, request, jsonify

class Policies(Resource):

    def get(self):

        return {"Message": "Please use post method instead."}, 200

    def post(self):
        # json_data = request.get_json(force=True)
        policies = []
        policies.append({
                "Company": "AIA Singapore",
                "Policy Name": "AIA Elite Secure Income (10 Pay)",
                "Premium Type": "Annual Premium",
                "Product Summary": "https://www.comparefirst.sg/wap/prodSummaryPdf/201106386R/WA_Sum_201106386R_ESI10P_Jan2022.pdf",
                "Features": [False, True, False, False, True],
            },
            {
                "Company": "AIA Singapore",
                "Policy Name": "AIA Elite Secure Income (5 Pay)",
                "Premium Type": "Annual Premium",
                "Product Summary": "https://www.comparefirst.sg/wap/prodSummaryPdf/201106386R/WA_Sum_201106386R_ESI5P_Jan2022.pdf",
                "Features": [False, True, False, False, True],
            },
            {
                "Company": "AIA Singapore",
                "Policy Name": "AIA Elite Secure Income (Single Pay)",
                "Premium Type": "Annual Premium",
                "Product Summary": "https://www.comparefirst.sg/wap/prodSummaryPdf/201106386R/WA_Sum_201106386R_ESISP_Jan2022.pdf",
                "Features": [False, True, True, False, True],
            })
        return {"Policies": policies}, 200
