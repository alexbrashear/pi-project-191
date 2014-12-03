from flask import Flask, request, redirect
from twilio.rest import TwilioRestClient
import twilio.twiml
import requests
import os
import sys

app = Flask(__name__)


ACCOUNT_SID = "AC6d1cfc62994ddb2ab8ad93758112e7c9" 
AUTH_TOKEN = "d9e9990762c20815b84d154310131e73" 

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

@app.route("/", methods=['GET', 'POST'])
def weatherResponse():
	"""Respond to incoming calls with a simple text message."""
	url = "http://api.wunderground.com/api/46666a893d350db6/conditions/q/PA/Philadelphia.json"
	forecast = requests.get(url).json()
	temp = forecast['current_observation']['temperature_string']
	wind = forecast['current_observation']['wind_string']
	feels_like = forecast['current_observation']['feelslike_string']
	humidity = forecast['current_observation']['relative_humidity']
	precip = forecast['current_observation']['precip_today_string']
	outlook = forecast['current_observation']['weather']
	msg = 'nothing entered'
	clientTextContent = request.values.get('Body').lower()
	if clientTextContent == 'menu':
		msg = 'options:\n\'outlook\' (i.e. partly cloudy)\n' + '\'temp\'\n' + '\'humidity\'\n' + '\'wind\'\n' + '\'feels like\'\n' + '\'humidity\'\n' + '\'precip\'\n' + '\'weather\'\n' + '\'hurricane\'\n'
	elif clientTextContent == 'outlook':
		msg = outlook
	elif clientTextContent == 'temp':
		msg = temp
	elif clientTextContent == 'wind':
		msg = wind
	elif clientTextContent == 'feels like':
		msg = feels_like
	elif clientTextContent == 'humidity':
		msg = humidity
	elif clientTextContent == 'precip':
		msg = precip
	elif clientTextContent == 'weather':
		msg = 'temperature: ' + temp + '\n' + 'outlook: ' + outlook + '\n' + 'wind: ' + wind + '\n' + 'feels like: ' + feels_like + '\n' + 'humidity: ' + humidity + '\n' + 'precip: ' + precip + '\n'
	elif clientTextContent == 'hurricane':
		msg = 'no hurricanes in your area'
	else:
		msg = "send \'menu\' to this number for a list of options"
	
	#resp = twilio.twiml.Response()
	#resp.message(msg)

	try:
		message = client.messages.create(to=request.values.get('From'), from_="+17576944797", body=msg)
	except Exception as e:
		print e

	return 'lorem ipsum'

if __name__ == "__main__":
	app.run(debug=True)
