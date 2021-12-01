import requests
from flask import Flask, request

app = Flask(__name__)

#@app.route('/auth')
#def userAuth():
 #   user = request.args.get('u')
  #  password = request.args.get('p')
   # if user != "tester" and password != "password":
    #   return f'Invalid user. Please try again'

@app.route('/city')
def searchCity():
    apiKey = 'bb26761eb813e25bfeb3b2b37911177b'
    user = request.args.get('u')
    password = request.args.get('p')
    if user != "tester" or password != "password":
        return f'Invalid user. Try Again.'

    city = request.args.get('q')
    
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={apiKey}'
    response = requests.get(url).json()
    if city.title() != "San Diego" and city.title() != "Tel Aviv":
        message = response.get('message', '')
        return f'Error getting teperature for {city.title()}. Please enter valid city.'

    if response.get('cod') != 200:
        message = response.get('message', '')
        return f'Error getting temperature for {city.title()}. Error message = {message}'

   
    curTemp = response.get('main', {}).get('temp')
    if curTemp:
        curTempF = round(((curTemp - 273.15)* 9/5)+ 32, 2)
        return f'Current temperature of {city.title()} is {curTempF} &#8457;'
    else:
        return f'Error getting temperature for {city.title()}'

@app.route('/')
def index():
	return '<h1>Welcome to my Weather App</h1>'


if __name__== '__main__':
	app.run(debug=True)

