from flask import Flask, send_from_directory
from flask_cors import CORS

def create_app(config_filename):
    application = app = Flask(__name__, static_url_path='')
    application.config.from_object(config_filename)
    cors = CORS(application, resources={r"/*": {"origins": "*"}})
    
    from api_links import api_bp
    application.register_blueprint(api_bp, url_prefix='/dev')

    return application


application = app =  create_app("config")

@application.route('/', methods=['GET'])
def index():
    return 'Api Running...'


if __name__ == "__main__":
    application.debug = True
    application.run()