from app import app
from flask import Flask,render_template, redirect, request, session, flash
from app.forms import PubContractSearch,ConcordeSearch
import requests as r
import os
import requests_oauthlib
from config import Config
from datetime import datetime
from app import utility as u

app.secret_key = Config.SECRET_KEY
app.debug = True

EVEESI = requests_oauthlib.OAuth2Session(Config.CLIENT_ID,
										scope = Config.SCOPES,
										redirect_uri = Config.REDIRECT_URI)

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
os.environ['OAUTHLIB_IGNORE_SCOPE_CHANGE'] = '1'

char_id = None
token = None
token_timestamp = None
api_data  = None

# ****************************************************************************
# Setup to grab login details and tokens
# TODO: Add refresh check. Tokens should have an expiry.
#

@app.route('/')
@app.route('/index')
def index():
	return render_template('homepage.html', title='Let\'s Login')

@app.route('/login')
def login():
	""" Prompt user to authenticate """
	auth_base = Config.AUTHORITY_URL + Config.AUTH_ENDPOINT
	authorization_url, state = EVEESI.authorization_url(auth_base)
	EVEESI.auth_state = state
	return redirect(authorization_url)

@app.route('/login/authorized')
def authorized():
	""" Handle callback from EVE auth """
	global token_timestamp
	#if request.query.state != EVEESI.auth_state:
	#	raise Exception('State returned to redirect URL does not match!')
	session['access_token'] = EVEESI.fetch_token(Config.AUTHORITY_URL + Config.TOKEN_ENDPOINT,
						client_secret = Config.CLIENT_SECRET,
						authorization_response = request.url)
	session['token_timestamp'] = datetime.now()

	return redirect('/login/get_char_id')
#	return redirect('/apicall')

@app.route('/login/get_char_id')
def get_char_id():
	global api_data
	global char_id
	# maybe don't store session vars in globals...
	global token
	token = session.get('access_token')['access_token']

	""" Get the character ID associated with the token """
	api_data = {'Authorization': 'Bearer ' + session.get('access_token')['access_token'],
				'Content-Type': 'application/json'}
	session['char_id'] = EVEESI.get(Config.AUTHORITY_URL + Config.VERIFY_ENDPOINT, headers=api_data).json()
	char_id = session['char_id'] # think about relying on session vars
	return redirect('/menu')
#	return redirect('/apicall')
#	return redirect('/stats')

#
# END setup section
@app.route('/dump')
def dump():
	""" Dump a block of data """
	return render_template('dump.html', data=session, title= "Session Data Dumper")

@app.route('/test')
def test():
	""" Test utility module """
	data = u.getPubContracts(10000031,90000000,100000000,Config,api_data)
#	data = u.getStructureName(1023425394442,Config,api_data)
#	flash('Length of returned data: {}'.format(len(data)))
	return render_template('pub_contracts.html', data=data, title="Utility Testing")
#	return render_template('dump.html', data=data, title="Utility Testing")

@app.route('/menu')
def menu():
	""" Display a menu of options """
	return render_template('menu.html', title = "Please Choose")

@app.route('/apicall')
def apicall():
	""" Verify token was obtained by getting user's public details """
	endpoint = 'characters/' + str(session['char_id']['CharacterID'])
	data = EVEESI.get(Config.QUERY_BASE + endpoint, headers=api_data).json()
	return render_template('apicall.html',
							graphdata = data,
							endpoint = endpoint,
							sample='EVE OAuth2 Flow')

@app.route('/location')
def location():
	""" Return current location of player. """
	if not u.check_token_time(session['access_token']):
		session['access_token'] = u.refresh_token(session['access_token'])
	endpoint = 'characters/' + str(session['char_id']['CharacterID']) + '/location'
	flash("Endpoint: {}".format(endpoint))
	data = EVEESI.get(Config.QUERY_BASE + endpoint, headers=api_data).json()
	return render_template('dump.html', data = data, title="Character Location") 

@app.route('/contracts')
def contracts():
	""" Return a list of player's contracts """
	endpoint = 'characters/' + char_id + '/contracts'
	data = EVEESI.get(Config.QUERY_BASE + endpoint, headers=api_data).json()
	return render_template('apicall.html',
							graphdata = data,
							endpoint = endpoint,
							sample = 'Character Contracts')

@app.route('/pubcontracts')
def pubcontracts():
	""" Return public contracts for given region """
	endpoint = "contracts/public/10000031/"
	data = EVEESI.get(Config.QUERY_BASE + endpoint, headers=api_data).json()
	return render_template('pub_contracts.html',
							data = data)

@app.route('/searchcontracts', methods=['GET', 'POST'])
def searchcontracts():
	form = PubContractSearch()
	if form.validate_on_submit():
		region = u.nameToId(form.region.data, 'REGION', Config, api_data)
		data = u.getPubContracts(region, form.min.data, form.max.data, Config, api_data, True, form.multiple.data)
		#flash('Searching {} ({}) for contracts priced between {} and {} isk. Multiple? {}'.format(form.region.data, region, form.min.data, form.max.data, form.multiple.data))
		return render_template('pub_contracts.html', data=data, title="Search Testing")
		#return render_template('menu.html', title='Please Choose')
	return render_template('search.html',title='Search Contracts',form=form)

@app.route('/concorde', methods=['GET', 'POST'])
def ospfconcorde():
	form = ConcordeSearch()
	if form.validate_on_submit():
		flash('Searching from {}'.format(form.start.data))
		return render_template('menu.html',title='Please Choose')
	return render_template('search.html', title='Nearest Concorde', form=form)

@app.route('/stats')
def stats():
	endpoint  = 'characters/' + str(session['char_id']['CharacterID']) + '/stats'
	data = EVEESI.get(Config.QUERY_BASE + endpoint, headers=api_data).json()[0]
	return render_template('stats.html', data=data, title='Character Stats')
