#!/usr/bin/python3
import urllib.request
import urllib.parse
import json
import pprint
import os.path

k = open('apikeyfile', 'r')
apikey = k.read()
k.close()

base_url = 'https://na.api.pvp.net/api/lol/na/v2.2/match'
match_url = '{0}/1900737521?api_key={1}'.format(base_url, apikey)
req = urllib.request.urlopen(match_url)
response = json.loads(req.read().decode("utf-8"))
champ_list =[]
for i in range(0,10):
	champ_list.append(response['participants'][i]['championId'])

