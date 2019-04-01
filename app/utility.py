import requests as r
from datetime import datetime
import pickle
import sys

# These caches will reduce the number of API calls to various endpoints
id_cache = {} # dict of int: string
name_cache = {} # dict of string:int

def check_token_time(token):
	""" Compare session variable token_timestamp
		against current time to determine if
		refresh is needed
	"""
	if datetime.now() < datetime.fromtimestamp(token['expires_at']):
		return True
	else:
		return False

def refresh_token():
	""" Obtain new token using refresh token
		if expired
	"""

def makePickles():
	pickle_dict = {'id':id_cache,'name':name_cache}
	with open('caches.pkl','wb') as f:
		pickle.dump(pickle_dict,f)

def eatPickles():
	global id_cache
	global name_cache
	
	with open('caches.pkl','rb') as f:
		pickle_dict = pickle.load(f)
		
	id_cache = pickle_dict['id']
	name_cache = pickle_dict['name']

def idToName(id, Config, api_data):
	""" Return a name for a given ID 

	Arguments:
	id: id value to be looked up
	Config: config object instantiated in routes.py
	api_data: header information from routes.py
	"""
	global name_cache
	global id_cache
	eatPickles()

	# TODO: handle lists of IDs
	if int(id) in id_cache: # this won't work for lists of IDs
		print('idToName cache hit')
		return id_cache[int(id)]
	api_body = str(id)
	response = r.post(Config.QUERY_BASE + 'universe/names/', headers=api_data, data = '[' + api_body + ']')
	data = response.json()[0]
	name = data['name']
	id_cache[id] = name
	if data['category'] == 'solar_system':
		if name not in system_cache:
			system_cache[name] = int(id)
	elif data['category'] == 'character':
		if name not in name_cache:
			name_cache[name] = int(id)
	makePickles()
	return name

def getStructureName(structure_id, Config, api_data):
	""" Return structure name for given ID

	Arguments:
	structure_id: id value to be looked up
	Config: config object instantiated in routes.py
	"""
	global id_cache
	global name_cache
	eatPickles()
	if structure_id not in id_cache or id_cache[structure_id] == '':
		query = "universe/structures/" + str(structure_id) + "/"
		data = r.get(Config.QUERY_BASE + query, headers=api_data).json()
		if 'name' in data.keys():
			id_cache[structure_id] = data['name']
			makePickles()
			return data['name']
		else:
			makePickles()
			return ''
	else:
		print("getStructureName cache hit")
		makePickles()
		return id_cache[structure_id]

def getPubContracts(region_id, min, max, Config, api_data, print=True, exclude_multiple=True):
	query = "contracts/public/" + str(region_id) + "/"
	contracts =  r.get(Config.QUERY_BASE + query, headers=api_data)
	if print == True:
		return _printContractDetails(contracts,min,max,Config,api_data,exclude_multiple)
	else:
		return contracts

def _getPubContractItems(contract_id,Config,api_data):
	query = "contracts/public/items/" + str(contract_id) + "/"
	return r.get(Config.QUERY_BASE + query, headers=api_data)

def _printContractDetails(contract_list,min,max,Config,api_data,exclude_multiple):
	""" Private method. Accepts a json object output by getPubContracts and prints details """
	contract_data = []
	for contract in contract_list.json():
		current = {}
		item_dict = {}
		if (contract['price'] >= min 
			and contract['price'] <= max 
			and contract['type'] == 'item_exchange'):
			items = _getPubContractItems(contract['contract_id'],Config,api_data).json()
			# this line is to exclude multiple-item contracts
			if exclude_multiple == True:
				if len(items) > 1:
					#print('.',end='')
					continue
			try:
				current['id'] = contract['contract_id']
				current['struct'] = getStructureName(contract['start_location_id'],Config,api_data)
				current['title'] = contract['title']
				current['issuer'] = idToName(contract['issuer_id'],Config,api_data)
				current['price'] = contract['price']
				current['date_issued'] = contract['date_issued']
				for item in items:
					item_dict[idToName(item['type_id'],Config,api_data)] = item['quantity']
				current['items'] = item_dict
				contract_data.append(current)
			except KeyError as e:
				print("KeyError: {}".format(e))
	makePickles()
	return contract_data
