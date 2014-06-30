#!/usr/bin/python
import requests
import requests.auth

def login():
	#API keys that authorize the script
	auth_script = requests.auth.HTTPBasicAuth('', '')
	#Login parameters for reddit account
	login_params = {
			"grant_type": "",
			"user_name": "",
			"password": "",
			"redirect_uri": "http://localhost"
			}
	access_url = "https://ssl.reddit.com/api/v1/access_token"
	response = requests.post(access_url, auth=auth_script, data=login_params)
	rc = int(response.status_code)	
	print rc
	print response.json()

if __name__ == "__main__":
	login()

