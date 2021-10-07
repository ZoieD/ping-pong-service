from flask import Flask
from werkzeug.wrappers import response
app = Flask(__name__)

import requests
@app.route('/')
def ping_service():
	return "Hello, I am ping service!"

@app.route('/ping')
def do_ping():
	ping = 'Ping ...'
	
	response = ''
	try:
		response = requests.get('http://pong-service-container:5001/pong')
	except requests.exceptions.RequestException as e:
		print('\n Cannot reach the pong serivce.')
		return 'Ping ...\n'

	return 'Ping ...' + response.text + '\n'


if __name__ == "__main__":
	app.run(host = '0.0.0.0', port = 5000, debug = True)