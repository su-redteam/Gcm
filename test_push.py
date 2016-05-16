from gcm import GCM
import requests.packages.urllib3
import RPi.GPIO as GPIO
import time

requests.packages.urllib3.disable_warnings()

GPIO.setmode(GPIO.BOARD)

pinvals = [29,31,7,11,13,15,19,21]
pinlist = range(0,len(pinvals))

GPIO.setup(pinvals[0], GPIO.IN) #Floor 1 status...
GPIO.setup(pinvals[1], GPIO.IN)
GPIO.setup(pinvals[2], GPIO.IN)
GPIO.setup(pinvals[3], GPIO.IN)
GPIO.setup(pinvals[4], GPIO.IN)
GPIO.setup(pinvals[5], GPIO.IN)
GPIO.setup(pinvals[6], GPIO.IN) #Master power status
GPIO.setup(pinvals[7], GPIO.IN) #Power Source gird?

ON = 'On'
OFF = 'Off'
GRID = 'Grid'
SOLAR = 'Solar'

floorlist = [OFF,OFF,OFF,OFF,OFF,OFF,OFF,GRID]

#GCM key
#gcm = GCM("AIzaSyB-DrluofQNo5Ov4YGxNrs6hpNuur2AfCI", debug = True)
gcm = GCM("AIzaSyB-DrluofQNo5Ov4YGxNrs6hpNuur2AfCI")


reg_id = ['dyQRQGGWixM:APA91bFkdnWkFwvvsA5vDLoBU-J90hPsjR1lh1SwTmNWWnyYdh__GJpAvz94gXc-D8YXlTKT-wDewkaZ0SJAIPjeFy3btEoOv-cMsmJMAjUg5JvL3ipzHe_Pu-BU2GO0nJwsdEbBWasv']

data = {'Floor1': floorlist[0], 'Floor2': floorlist[1],'Floor3':floorlist[2],'Floor4':floorlist[3],'Floor5':floorlist[4],'Floor6':floorlist[5],'Master':floorlist[6],'Power':floorlist[7]}

response = gcm.json_request(registration_ids=reg_id, data=data)

while True:
    for i in pinlist:
        currentpin = pinvals[i]
        if (GPIO.input(currentpin) == 1):
            if (i < 7):
                floorlist[i] = ON
            else:
                floorlist[i] = SOLAR
        else:
            if (i < 7):
                floorlist[i] = OFF
            else:
                floorlist[i] = GRID
    
    data = {'Floor1': floorlist[0], 'Floor2': floorlist[1],'Floor3':floorlist[2],'Floor4':floorlist[3],'Floor5':floorlist[4],'Floor6':floorlist[5],'Master':floorlist[6],'Power':floorlist[7]}

    response = gcm.json_request(registration_ids=reg_id, data=data)

    print(response)

    time.sleep(1)
