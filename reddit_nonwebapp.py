#!/usr/bin/python
import requests
import time
from pprint import pprint
import json
import os

CLIENT_ID = ""
CLIENT_SECRET = ""

#def key_in_file():
#	with open('key.txt') as f:
#		if (time.ctime(os.path.getmtime(f)) > 3600:
#			get_a_new_key()
#		else:
#			use_existing()
			
def login():
	#API keys that authorize the script
	auth_script = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
	
	#Login parameters for reddit account
	login_params = {
			'grant_type': 'password',
			'username': '',
			'password': '',
			'redirect_uri': 'http://localhost'
			}
	access_url = 'https://ssl.reddit.com/api/v1/access_token?'
	login_attempt = 0
	while login_attempt < 5:
		response = requests.post(access_url, data=login_params, auth=auth_script)
		rc = int(response.status_code)
		if 

		elif rc == 429:
			login_attempt += 1
			print "Attempting to login again"
			time.sleep(2)
		elif rc == 200:
			print rc
			with open('key.txt', 'w+') as f:
				resp_list = response.json()
				at = resp_list['access_token']
				f.write(at)
				f.close()
			break
		elif login_attempt == 5:
			print "Could not get a token with alloted number of attempts. Script will exit."
			break
			exit()
		else:
			print rc
			break
			exit()
	return at
	

if __name__ == "__main__":
	headers = {
			"Authorization": "bearer %s" % login(),
			"User-Agent": "stoicaureliusscript/1.0 by stoicaurelius"}
	access_url = "https://oauth.reddit.com/api/v1/me/karma"
	response = requests.get(access_url, headers=headers)
	data = json.loads(response.text)
	print str(data['data'][0]['comment_karma']) + ' ' + str(data['data'][0]['sr'])

