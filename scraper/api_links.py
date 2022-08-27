from flask import Blueprint
from flask_restful import Api

from resources.scraper import Scraper
from resources.policies import Policies

api_bp = Blueprint("api", __name__)
api = Api(api_bp)

api.add_resource(Scraper, "/scrape")
api.add_resource(Policies, "/policies")