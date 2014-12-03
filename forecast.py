import requests
import os
import re
from datetime import datetime

API_KEY = "46666a893d350db6"

def getWeather():
	url = "http://api.wunderground.com/api/" + API_KEY + "/conditions/q/PA/Philadelphia.json"
	forecast = requests.get(url).json()
	observation_time = datetime.now().strftime("%I:%M %p")
	temp = str(forecast['current_observation']['temp_f'])
	weather = str(forecast['current_observation']['weather'])
	return observation_time + ", " + temp + "F\n" + weather
	
