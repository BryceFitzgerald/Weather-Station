from Measurement import Measurement
from LLQueue import LLQueue
from LLNode import LLNode
from TemperatureSensor import TemperatureSensor
from PressureSensor import PressureSensor
import datetime
import socket

import random, string

import threading
import time





class measurementCache():
    def __init__(self, tempSensor, pressSensor):
        self.tempSensor = tempSensor
        self.pressSensor = pressSensor
        self.cache = LLQueue()
        self.length = self.cache.length
        self.sensorControl = False
        self.thread = None

    def updateCache(self):
        measurement = Measurement(self.tempSensor, self.pressSensor)
        self.cache.EnQueue(measurement)
        self.length += 1

    def pull(self):
        return self.cache.DeQueue()
        self.length = self.length - 1

    def backgroundMeasurementCycle(self):
        while self.sensorControl == True:
            self.updateCache()
            time.sleep(0.5)

    def runBackgroundMeasurementCycle(self):
        self.thread = threading.Thread(target=self.backgroundMeasurementCycle, daemon=True)
        self.thread.start()

    def printCache(self):
    	while self.length > 0:
    	    print(str(self.pull()) + "\n")
    	    time.sleep(.1)
    	    print(self.length)

    def crashBackgroundMeasurementCycle(self):
        self.thread.join()
        

# Function that generates random alpha numaric string 16 characters long
def genAddress():
    addr = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return addr

# announcement to terminal. might add anouncement storage feature to future update
def announce(subject, message):
    print(str(datetime.datetime.now())+""+ subject + ": " + message)










def Main():
    #Constant values and global control variables
    #----------------------------------------------------------------------------------------------------
    # global server Commands
    SERVER_COMMANDS = ["STOP_SERVER", "DATA_RECIEVED_TRUE", "DATA_RECIEVED_FALSE", "END_DATA_TRANSFER","START_DATA_TRANSFER"]
    
    # server connection status
    serverConnected = False 


    #server host and port
    HOST = '192.168.56.1'
    PORT = 5000

    #recieved data
    data = None
    #----------------------------------------------------------------------------------------------------
    
    # CONNECT SENSORS
    tempSensor = TemperatureSensor(genAddress(), 4)
    pressSensor = PressureSensor(genAddress(), 7)

    announce("SERVER", "Sensors Connected\nPressure Sensor:\tAddress: " + pressSensor.sensorAddress+"\tGPIO Pin: "+str(pressSensor.gpio)+"\nTemperature Sensor:\tAddress: " + tempSensor.sensorAddress + "\tGPIO Pin: " + str(tempSensor.gpio))
    

    # Create Cache
    cache = measurementCache(tempSensor, pressSensor)

    # Create Server
    s = socket.socket() # create socket object
    s.bind((HOST, PORT)) # bind host and port to Socket Object

    # listen for connnection to Server and accept new connection
    s.listen(1) # begin listening for new connection ( one at a time)
    c, addr = s.accept() # returns a new socket connection c and address addr
    announce("SERVER", "Server connected to Client: " + str(addr)) # announce server connection

    #begin background sensor datat recording and storing
    cache.sensorControl = True # set sensor control variable to true
    cache.runBackgroundMeasurementCycle()
    time.sleep(5)
    cache.sensorControl = False
    print(cache.length)

    cache.printCache()

    print(cache.length)





    
    # listen for send Command

    # send Data
    # send end Command
    # continuous Loop
    # listen for send / stop comomand
    # send data
    # send finised sending command

    # announce shutdown
    announce("SERVER", "PROGRAM COMPLEATED")





if __name__ == '__main__':
	Main()