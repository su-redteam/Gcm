from gcm import GCM
import requests.packages.urllib3
import RPi.GPIO as GPIO
import time

requests.packages.urllib3.disable_warnings()

GPIO.setmode(GPIO.BOARD)

#The board number for the usable pins
pinvals = [12,13,15,16,18,22,11,29]
pinlist = range(0,len(pinvals))
powerrelaypin = 36;
shutdownpin = 31;

GPIO.setup(pinvals[0], GPIO.IN) #Floor 1 status...
GPIO.setup(pinvals[1], GPIO.IN)
GPIO.setup(pinvals[2], GPIO.IN)
GPIO.setup(pinvals[3], GPIO.IN)
GPIO.setup(pinvals[4], GPIO.IN)
GPIO.setup(pinvals[5], GPIO.IN)
GPIO.setup(pinvals[6], GPIO.IN)  #Master power status
GPIO.setup(pinvals[7], GPIO.IN)  #Power Source gird/solar
GPIO.setup(shutdownpin, GPIO.IN) #Shutdown switch
GPIO.setup(powerrelaypin, GPIO.OUT) #Toggles the relay for power status

#Status Types
ON = 'On'
OFF = 'Off'
GRID = 'Grid'
SOLAR = 'Solar'

#Initial status
floorlist = [OFF,OFF,OFF,OFF,OFF,OFF,OFF,GRID]

#GCM key
#gcm = GCM("AIzaSyB-DrluofQNo5Ov4YGxNrs6hpNuur2AfCI", debug = True)
#gcm = GCM("AIzaSyB-DrluofQNo5Ov4YGxNrs6hpNuur2AfCI")
gcm = GCM("AIzaSyBTW6A2s7AJht-ilzoTeVG8x4LwgAkfONM")

#This is specific to each phone
reg_id = ['dyQRQGGWixM:APA91bFkdnWkFwvvsA5vDLoBU-J90hPsjR1lh1SwTmNWWnyYdh__GJpAvz94gXc-D8YXlTKT-wDewkaZ0SJAIPjeFy3btEoOv-cMsmJMAjUg5JvL3ipzHe_Pu-BU2GO0nJwsdEbBWasv']

#Data packet initialize
data = {'Floor1': floorlist[0], 'Floor2': floorlist[1],'Floor3':floorlist[2],'Floor4':floorlist[3],'Floor5':floorlist[4],'Floor6':floorlist[5],'Master':floorlist[6],'Power':floorlist[7]}

response = gcm.json_request(registration_ids=reg_id, data=data)

#Send Status
while 1:
#while (GPIO.input(shutdownpin) == 0):

    #Toggle Relay
    powerin = pinvals[7]
    if (GPIO.input(powerin) == 0):
        #GPIO.output(powerrelaypin,1)
        GPIO.output(powerrelaypin,0)
        print('1')
    else:
        #GPIO.output(powerrelaypin,0)
        GPIO.output(powerrelaypin,1)
        print('2')


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
