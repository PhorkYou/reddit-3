#!/usr/bin/python
import requests
import requests.auth
import time
from pprint import pprint

CLIENT_ID = ""
CLIENT_SECRET = ""

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
		if rc == 429:
			login_attempt += 1
			print "Attempting to login again"
			time.sleep(2)
		elif rc == 200:
			print rc
			break
		elif login_attempt == 5:
			print "Could not get a token with alloted number of attempts. Script will exit."
			break
			exit()
		else:
			print rc
			break
			exit()
	resp_list = response.json()
	at = resp_list['access_token']
	return at
	

if __name__ == "__main__":
	headers = {"Authorization": "bearer %s" % login()}
	response = requests.get("https://oauth.reddit.com", headers=headers)
	print pprint(response.text)

