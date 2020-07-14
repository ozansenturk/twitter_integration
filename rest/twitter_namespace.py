from flask_restx import Namespace, Resource, fields
import http.client
import json
from backend import services
import logging


logging.basicConfig(level=logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(logging.Formatter(
                 '%(asctime)s %(levelname)s: %(message)s '
                 '[in %(pathname)s:%(lineno)d]'))

api_ns = Namespace('api', description='Twitter management')

api_ns.logger.addHandler(stream_handler)

token_request = api_ns.model('token_request', {
    'client_id':fields.String(description='Twiter API Key'),
    'client_secret':fields.String(description='Twitter API Secret')
})
token_response = api_ns.model('token_response', {
    'token_type':fields.String(description='Token type'),
    'access_token':fields.String(description='Bearer token')
})

search_request = api_ns.model('token_request', {
    'client_id':fields.String(description='Twiter API Key'),
    'client_secret':fields.String(description='Twitter API Secret')
})
search_response = api_ns.model('token_response', {
    'token_type':fields.String(description='Token type'),
    'access_token':fields.String(description='Bearer token')
})

search_response = api_ns.model('search_response', {
    'created_at':fields.String(description='Creation time'),
    'id_str':fields.String(description='User Id'),
    'text':fields.String(description='Tweet')
})

search_responses = api_ns.model('search_responses', {
    'statuses':fields.List(fields.Nested(search_response))
})

search_parser = api_ns.parser()
search_parser.add_argument('q', type=str),
search_parser.add_argument('result_type', type=str);
search_parser.add_argument('count', type=int)

@api_ns.route('/get_token/')
class Token(Resource):

    @api_ns.doc('Getting access token')
    @api_ns.expect(token_request)
    @api_ns.marshal_with(token_response, code=http.client.OK)
    def post(self):
        '''Get tweets'''

        data = api_ns.payload
        api_ns.logger.debug("data {}".format(data))

        response_token = services.get_bearer_token(data["client_id"], data["client_secret"])

        api_ns.logger.debug("response_token {}".format(response_token))

        return response_token.json()


@api_ns.route('/search/')
@api_ns.expect(search_parser)
class SearchTweets(Resource):

    @api_ns.doc('Search tweet')
    @api_ns.marshal_with(search_responses, code=http.client.OK)
    def get(self):
        '''Get tweets'''

        params = search_parser.parse_args()

        api_ns.logger.debug("args {}".format(params))

        response = services.search_tweets(params)

        api_ns.logger.debug("response {}".format(response))

        return response.json()
