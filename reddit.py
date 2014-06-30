#!/usr/bin/python

from flask import Flask
import requests
from uuid import uuid4
import urllib

CLIENT_ID = ""
CLIENT_SECRET = ""
REDIRECT_URI = "http://localhost:5000"

app = Flask(__name__)
@app.route('/')

def homepage():
	text = '<a href="%s">Authenticate reddit API session</a>'
	return text % create_auth_url()

def create_auth_url():
	state = str(uuid4())
	#save_state(state)
	auth = {'client_id': CLIENT_ID,
		'response_type': 'code',
		'state': state,
		'redirect_uri': REDIRECT_URI,
		'duration': 'temporary',
		'scope': 'identity'}
	base_url = "https://ssl.reddit.com/api/v1/authorize"
	auth_url = requests.get(base_url, params=auth)
	return auth_url.url

if __name__ == "__main__":
	app.run(debug=True)
