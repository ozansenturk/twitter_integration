from flask_restx import Api
from flask import Flask
from .twitter_namespace import api_ns
import logging


api = Api(version='0.1', title='Twitter Integration',
          description='Tweet management')
api.add_namespace(api_ns)

def create_app(config_name):

    from config import config
    from werkzeug.middleware.proxy_fix import ProxyFix

    application = Flask(__name__)
    application.config.from_object(config[config_name])
    config[config_name].init_app(application)
    application.wsgi_app = ProxyFix(application.wsgi_app)

    if not application.debug and not application.testing:

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'))
        # stream_handler.setLevel(logging.DEBUG)
        application.logger.addHandler(stream_handler)

        application.logger.setLevel(logging.DEBUG)
        application.logger.info('Twitter management startup')

    return application
