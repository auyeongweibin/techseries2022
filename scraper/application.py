from flask import Flask, send_from_directory
from flask_cors import CORS
from boto3 import client, resource
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, REGION_NAME

client = client(
    'dynamodb',
    aws_access_key_id     = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
    region_name           = REGION_NAME,
)

resource = resource(
    'dynamodb',
    aws_access_key_id     = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
    region_name           = REGION_NAME,
)

policies_db = resource.Table('Policies')

def create_app(config_filename):
    application = app = Flask(__name__, static_url_path='')
    application.config.from_object(config_filename)
    cors = CORS(application, resources={r"/*": {"origins": "*"}})
    
    from api_links import api_bp
    application.register_blueprint(api_bp, url_prefix='/dev')

    return application


application = app =  create_app("config")

@application.route('/.well-known/<path:path>')
def send_js(path):
    return send_from_directory('.well-known', path)

@application.route('/', methods=['GET'])
def index():
    return 'Api Running...'


if __name__ == "__main__":
    application.debug = True
    application.run()