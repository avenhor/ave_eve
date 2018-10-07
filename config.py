import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess-me-puto'
	CLIENT_ID = 'c5fc71083eaa4683acc7ab0107b2852a'
	CLIENT_SECRET = 'WkLiJOzG68Y9cJVO2pn2nlcTLJXwb9KUSGcmvbVP'
	REDIRECT_URI = 'http://localhost:5000/login/authorized'

	AUTHORITY_URL = 'https://login.eveonline.com'

	AUTH_ENDPOINT = '/oauth/authorize'
	TOKEN_ENDPOINT = '/oauth/token'
	VERIFY_ENDPOINT = '/oauth/verify'

	SCOPES = ['publicData','esi-location.read_location.v1','esi-wallet.read_character_wallet.v1','esi-universe.read_structures.v1']

	QUERY_BASE = 'https://esi.tech.ccp.is/latest/'
