# import the things

import measurement
import announcer
import pressureSensor
import temperatureSensor
import socket
import threading
import datetime
import random 
import string
import measurementCache

class server:
	# Generates 16 digit alphanumeric string
    def generateAddress():
    	# taken from stack overflow (THX David Nathan)
        addr = ''.join(random.choices(string.ascii_letters + string.digits, k =16)) 
        return addr

    def __init__(self, host, port, gpio1, gpio2):
        # define globalRuntimeIndicator boolean 
        self.globalRuntimeIndicator = True

        # define socket Constant values
        self.HOST = host
        self.PORT = port

        # define sensors
        self.temperatureSensor = temperatureSensor(generateAddress(), gpio1)
        self.pressureSensor = pressureSensor(generateAddress(), gpio2)

        # define cache
        self.cache = measurementCache(temperatureSensor, pressureSensor)

        # define background measurement sequenceThread
        bMSThread = threading.Thread(target="bMSequence", daemon=True)
        
        # define announcer 'filename = log.csv'
        self.logFilename = 'log.csv'
        logger = announcer(self.logFilename)

        # define socket
        s = socket.socket() # create socket object

        # initiate startup sequence
        startupSequence()


    def startupSequence(self):
        bindSensors()
        createSocket()
        establishHandshake()
    
    def mainLoop(self):
        startBMSThread()
        while globalRuntimeIndicator == True:
            beamData()
            listenForCommands()
        beamData()






