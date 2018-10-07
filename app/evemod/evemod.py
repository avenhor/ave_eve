%matplotlib inline

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import requests as r, json
from datetime import datetime
import pickle
import networkx as nx

auth_base = "https://login.eveonline.com/oauth/token"
avenhor_client_id = "2898ef8e62584cbd98b2ec8295d2bbba"
avenhor_client_secret = "N57a2mDLMOaAPz2DN1il8HD7ht3UftdqgTruejVa"
avenhor_refresh_token = "MtUGBuWZi3rmJ5EJ4M_zcIXKh_MtUtBUCPSsTGYHfPHva8QnzPidUfJqeVj9Te4SFYb6HGJsxlpWCHOOIkYKmTgkUfU4tD9Fa0wN9ffnqkYbO-FiC4-7vYJVGEvEXRZqWCeKs8UPcHOt7tKBcmBlf9gPWl1Su8r0nGE_SMe3OawwDLe52AQuW4-1GMPaGozPVwRDO3eodSk6RXCiMoAybu0mMQdtDfHDO77UvLcuosPT5EODpWrPOsJhVhHq4fMgm5soiefxEvKP3L0sU9vie6bSQajYMoFKlBcVDwN_b0z-j2Oc8pvlUD46uER-p1qWJYsiZVYB-0LmoZmzT_JYeeV9enemLDGmUEb2MBzjuGykK1KZLP_BfiuVCZWIh491Dx8eBPW-YKD55HB3wsETyjj_pBxlsNOFZEHQNCEZTN9ze2bNX3GQbUBIvuh7hCAxsSwbMVh66M0m7KSH9UrFalJO4CLTCbijJgP9CtOw84vJlZ3Jav5B_U3H3vguB74s8-RG7_rRutoFsL_kYSRzgfV9aT12Tb9_d5CJVCqBtKeZeIAhlKXZBVhCWNd3qVo4TwtFQfYl1crJ00xTKF2IRmnB3h2SwM4fMjtwfZqSVp8TB2EgqYfbkhanoVJZ0UTLONwsILzW-n768pGg9uhFrA2"
parke_client_id = "1333d6a7d2dc403c85c85d92b33c1793"
parke_client_secret = "MUGuDDsQwYKgmuvSLQpB5SoFvwJIbrkmD6mnJ5bz"
parke_refresh_token = "_6R7y4q_gzRsBIleVuN9ygWDo0i75eu5Vx20COElrbaZQUpk9HV_Np4anit2Jt_mcr5uz5GhZopQbPwyMWIf4J5cq3LV8xkFGrgwwxkqG15YZip3nSH8MKfnkvjcNwsGfLPdw5LYsXWUlKcX0DLWUlUGaIXyXE1Y6BB32LswMQ42HRk7O-eL6q3HTi1XndN7UI3jb4w2r9uLP77XMpT7DK32Klxhed3sHU7UqptFeWphVaHZXgnKNy7_x1x3vtDeMoBo5HbQwbDBlSdD9H8Hp3q9Sz3gw-2w7FbEYV-unPnRr1tBWzlIEDi2JpoE_npv6uAlvJb5gLc9MecbXT7g6G1ZtiCUOxajNFB2Z1EryusgiJu_cvbrH4tWNjnwCnZWgDNuT89iOfEqP2gBddowh_mcmXnvuxLXEAToCTEEcMVtOfZZnmUeP2SABuBRFS7NosUxS4wNi_fTihYGHusgQVges56sQb05ClVFIlnMOtukSTJj2kKFcdm7EeZFaa9KU-4VYGs_XZ_wpH5jEqO8m70DrU0a3ZvOwypMybtoXTrTgizqh4hPf88VEgfi0sF3idyhp5Y0VXvr8rKxTG5YFIIAVlif7QE5C5_ZILPPiZAK1XgKxRU5bngDwShEKeDsVaIS5FQF4IIXhC4bQn1u1w2"
yella_client_id = "c62d88e9838545a09282d43331800feb"
yella_client_secret = "XoiHjJB2G63j0ufJYjISUB7Cp6JxiuGYyg9xMnrC"
yella_refresh_token = "rMzSZmFhxSAOVJYLuCHIkl3oO0ghJnpUrdvUXWtM6292L3I-S5uAOxk1uiqfnA4f0"
grant_type = "refresh_token"
avenhor_char_id = '96960191'
meeseeks_char_id = '2112778678'
parke_char_id = '2113415144'
yella_char_id = '2113693888'
avenhor_data = {'client_id': avenhor_client_id, 'client_secret': avenhor_client_secret, 'refresh_token': avenhor_refresh_token, 'grant_type': grant_type}
parke_data = {'client_id': parke_client_id, 'client_secret': parke_client_secret, 'refresh_token': parke_refresh_token, 'grant_type': grant_type}
yella_data = {'client_id': yella_client_id, 'client_secret': yella_client_secret, 'refresh_token': yella_refresh_token, 'grant_type': grant_type}
concord = ['Avada','Chibi','Haimeh','Mishi','Pahineh','Asabona','Chidah','Sendaya','Shamahi','Sooma','Adeel','Groothese','Mormelot','Olide','Kemerk','Pakhshi','Tekaima','Yulai','Agil','Ipref','Kihtaled','Neyi','Keproh','Rannoze','Zatamaka','Arvasaras','Autaris','Jan','Vellaine','Geffur','Hilfhurmur','Lumegen','Oppold','Tratokard','Arlulf','Brundakur','Nedegulf','Stirht','Altbrard','Half','Hedaleolfarber','Istodard','Aeditide','Egbinger','Klingt','Aulbres','Barleguet','Assiettes','Esmes','Goinard','Lermireve','Raeghoscon','Hatakani','Iivinen','Tennen','Yashunen','Mastakomon','Uchoshi']
query_base = 'https://esi.tech.ccp.is/latest/'
api_data = None
# G = nx.Graph # a basic graph that holds the entire eve universe

# These caches will reduce the number of API calls to various endpoints
id_cache = {} # dict of int: string
name_cache = {} # dict of string:int
sec_cache = {}
kills_cache = {}
kills_cache_timestamp = None
system_cache = {} # dict of string:int
id_cache_miss = 0
id_cache_hit = 0
name_cache_miss = 0
name_cache_hit = 0

def makePickles():
    pickle_dict = {'id':id_cache,'name':name_cache,'sec':sec_cache,'kills':kills_cache,
                   'kills_age':kills_cache_timestamp,'system':system_cache,'eve_map':G}
    with open('dill.pkl','wb') as f:
        pickle.dump(pickle_dict,f)
        
def eatPickles():
    global id_cache
    global name_cache
    global sec_cache
    global kills_cache
    global kills_cache_timestamp
    global system_cache
    global G
    
    with open('dill.pkl','rb') as f:
        pickle_dict = pickle.load(f)
        
    id_cache = pickle_dict['id']
    name_cache = pickle_dict['name']
    sec_cache = pickle_dict['sec']
    kills_cache = pickle_dict['kills']
    kills_cache_timestamp = pickle_dict['kills_age']
    system_cache = pickle_dict['system']
    G = pickle_dict['eve_map']
    
def getContracts(id):
    return r.get(query_base + 'characters/' + id + '/contracts', headers = api_data)

def getLocation(id):
    response = r.get(query_base + 'characters/' + id + '/location', headers = api_data)
    return response.json()['solar_system_id']

def idToName(id):
    global name_cache
    # TODO: handle lists of IDs
    if int(id) in id_cache: # this won't work for lists of IDs
        return id_cache[int(id)]
    api_body = str(id)
    response = r.post(query_base + 'universe/names/', headers=api_data, data = '[' + api_body + ']')
    data = response.json()[0]
    name = data['name']
    id_cache[id] = name
    if data['category'] == 'solar_system':
        if name not in system_cache:
            system_cache[name] = int(id)
    elif data['category'] == 'character':
        if name not in name_cache:
            name_cache[name] = int(id)
    return name

# def nameToId(name):
#     global id_cache
#     # TODO: handle lists of names
#     if name in name_cache:
#         return name_cache[name]
#     if name.upper() == 'JITA':
#         id = 30000142
#     else:
#         api_body = '[\"' + name + '\"]'
#         response = r.post(query_base + 'universe/ids/', headers=api_data, data=api_body)
#         id = int(response.json()['systems'][0]['id'])
#     if id not in id_cache:
#         id_cache[id] = name
#     return id

def nameToId(name,qryType):
    global id_cache
    # TODO: handle lists of names
    if name in name_cache:
        return name_cache[name]
    if name.upper() == 'JITA':
        id = 30000142
    else:
        api_body = '[\"' + name + '\"]'
        response = r.post(query_base + 'universe/ids/', headers=api_data, data=api_body)
        if qryType.upper() == 'SYSTEM':
            id = int(response.json()['systems'][0]['id'])
        elif qryType.upper() == 'CHAR':
            id = int(response.json()['characters'][0]['id'])
    if id not in id_cache:
        id_cache[id] = name
    return id

def plotBalance():
    plt.figure(figsize=(20,10))
    plt.plot(dates, bal, color='blue', marker='.', linestyle='solid')
    plt.title("Account Balance")
    plt.ylabel("Billions of ISK")
    plt.ticklabel_format(style='sci', axis='y', useOffset=10)
    plt.xlabel("Date")
    plt.show()
    
def printJournal(result):
    global id_cache
    cache_hits = 0
    cache_misses = 0
    for x in result.json():
        reason = x['ref_type']
        date = datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%SZ')
        if ('first_party_id' in x and 'second_party_id' in x):
            if (int(x['first_party_id']) in id_cache):
                cache_hits += 1
                p1 = id_cache[int(x['first_party_id'])]
            else:
                cache_misses += 1
                p1 = idToName(x['first_party_id'])
                id_cache[int(x['first_party_id'])] = p1
            if (int(x['second_party_id']) in id_cache):
                cache_hits += 1
                p2 = id_cache[int(x['second_party_id'])]
            else:
                cache_misses += 1
                p2 = idToName(x['second_party_id'])
                id_cache[int(x['second_party_id'])] = p2
            amount = x['amount']
            print("{}: {}: {}: {:,.2f}\t{}\n\th: {} / m:{}".format(date,p1,p2,amount,reason,cache_hits,cache_misses))    
            
def getTokens():
    avenhor_token = r.post(auth_base, data = avenhor_data)
    parke_token = r.post(auth_base, data = parke_data)
    yella_token = r.post(auth_base, data= yella_data)
    return (avenhor_token,parke_token,yella_token)

def getSecStatus(id):
    if int(id) in sec_cache:
        return sec_cache[int(id)]
    else:
        sec = r.get(query_base + 'universe/systems/' + str(id)).json()['security_status']
        sec_cache[int(id)] = sec
        return sec
    
def getShipKills():
    global kills_cache
    global kills_cache_timestamp
    if kills_cache_timestamp is not None:        
        diff = datetime.now() - kills_cache_timestamp
        if diff.seconds > 3600:
            print('Generating new kills cache')
            kills = r.get(query_base + 'universe/system_kills/')
            for x in kills.json():
                kills_cache[int(x['system_id'])] = x['ship_kills']
            kills_cache_timestamp = datetime.now()
        else:
            print('Using existing kills cache')
    else:
        print('Generating new kills cache')
        kills = r.get(query_base + 'universe/system_kills/')
        for x in kills.json():
            kills_cache[int(x['system_id'])] = x['ship_kills']
        kills_cache_timestamp = datetime.now()
        
def loadConcordCache():
    for x in concord:
        if x not in system_cache:
            system_cache[x] = nameToId(x,'system')
            
def ospConcord(*args):
    shortest_path = None
    shortest_path_system = ''
    shortest_route = None
    if args is not None and len(args) != 0:
        loc = nameToId(args[0],'system')
    else:
        loc = getLocation(char_id)
    myloc = idToName(loc)
    print('Starting search in {}'.format(myloc))

    for x in concord:
        if x == 'Amarr':
            continue
        if (myloc in system_cache and x in system_cache):
            route = getRoute(system_cache[myloc],system_cache[x],'','secure')
        else:
            route = getRoute(nameToId(myloc,'system'),nameToId(x,'system'),'','secure')
        route_len = len(route.json())
        if shortest_path is None or route_len < shortest_path:
            shortest_path_system = x
            shortest_path = route_len
            shortest_route = route
        if route_len < 10:
            print('***************** {} -> {}'.format(myloc,x))
            printRoute(route)
        print('{}: {}'.format(x,len(route.json())))
    print('*****************')
    print('*****************')
    print('{} is closest system at {} jumps'.format(shortest_path_system,shortest_path))
    print('***************** {} -> {}'.format(myloc,shortest_path_system))
    printRoute(shortest_route)
    
def getRoute(origin,destination,avoid,flag):
    '''
    Flag can be shortest,secure,insecure,or blank
    '''
    param = ''
    query = 'route/' + str(origin) + '/' + str(destination)
    if (avoid != '' and avoid is not None):
        param = '/?avoid='
        if isinstance(avoid,int):
            param += str(avoid)
        elif isinstance(avoid,list):
            for a in avoid:
                param += str(a) + ','
            param = param[:-1]
    if (flag != '' and flag is not None):
        if (avoid != '' and avoid is not None):
            param += '&flag='
        else:
            param += '/?flag='
        param += flag
    query = 'route/' + str(origin) + '/' + str(destination) + param
    return r.get(query_base + query, headers=api_data)

def printRoute(route):
    for x in route.json():
        name = ''
        secStatus = 0
        kills = 0
        global kills_cache
        
        # check if system is in id cache
        if int(x) in id_cache:
            name = id_cache[int(x)]
        else:
            name = idToName(x)
            id_cache[int(x)] = name
        # add system to cache if not present
        if name not in system_cache:
            system_cache[name] = int(x)
        # check if id is in system kills cache
        if x in kills_cache:
            kills = kills_cache[x]
        else:
            kills = 0
            kills_cache[x] = 0
        print('{:<20}{:4.1f}\t{:>4} {:>16}'.format(id_cache[int(x)],float(getSecStatus(x)),kills,'kills last hour'))
        
def main():
    global api_data
    global char_id
    global token
    global access_token
    
    print('Loading pickled caches...\n')
    eatPickles()
    print('Grabbing tokens...\n')
    avenhor_token, parke_token, yella_token = getTokens()

    token = avenhor_token
    char_id = avenhor_char_id
    
#     token = yella_token
#     char_id = yella_char_id

    # char_id = meeseeks_char_id

    # token = parke_token
    # char_id = parke_char_id

    access_token = token.json()['access_token']
    
    api_data = {'Authorization': 'Bearer ' + access_token, 'Content-Type': 'application/json'}
    
    print('Loading the Concord cache...')
    loadConcordCache()
    print('Checking ship kills cache...')
    getShipKills()
    print('Pickling caches and vars...')
    makePickles()
    print('Done')
    
def refresh_tokens():
    print('Grabbing tokens...\n')
    avenhor_token, parke_token, yella_token = getTokens()

    token = avenhor_token
    char_id = avenhor_char_id
    
#     token = yella_token
#     char_id = yella_char_id

    # char_id = meeseeks_char_id

    # token = parke_token
    # char_id = parke_char_id

    access_token = token.json()['access_token']
    
    api_data = {'Authorization': 'Bearer ' + access_token, 'Content-Type': 'application/json'}
    print('Tokens updated')
