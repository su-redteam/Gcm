#app.py
#Loren Klemesrud
#This code will control the pins going to our relays and create a web server to access the information
from flask import Flask
from flask import json
import RPi.GPIO as GPIO

#Pin Definitions
pintest = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(pintest, GPIO.OUT)
GPIO.output(pintest,GPIO.LOW)

#Default Floor Status
F1 = "OFF"
F2 = "OFF"
F3 = "OFF"

app = Flask(__name__)

#Create Server
@app.route('/')
def index():
    return 'Hello world'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

jsonify(Floor1 = F1, Floor2 = F2, Floor3 = F3)

#Save Status as JSON data
@app.route('/status', methods = ['GET'])
def api_status():
    data = {
        'Floor1'  : F1,
        'Floor2'  : F2
    }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://luisrei.com'

    return resp
