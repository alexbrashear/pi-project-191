pi-project-191
==============

Snowberry Pi

User Instructions:
1. Once Raspberry PI is turned on, the LCD screen should display the weather information and update every minute.
2. Text 'menu' to +1 (757) 694-4797, which is the Twilio number for the Raspberry Pi, for a list of request options.

Important Python Files:
run.py
-This python program launches a server. Whenever a user texts the twilio number, the server will receive the text, parse it using python, and send an appropriate response based on the content of the request. 
-Server is set up using ngrok, which maps public ip address to localhost.
-ngrok and and run.py are called in .bash_profile when shell starts after boot. We eliminated the login to streamline the process. 

displayWeather.py
-Displays weather, current time, and outlook on LCD screen using Weather Underground API.
-Main program is in forecast.py. displayWeather.py sets up connection with LCD and calls the program in forecast.
-Daemon in crontab is setup so that the LCD screen gets updated every minute when the Raspberry Pi is on.
