# import sensor object
import sensor

# import abstract class libraries (ABC = abstact parent class, abstractmethod = method decorator)
from abc import ABC, abstractmethod

class temperatureSensor(sensor.sensor):
    def __init__(self, sensorAddress, gpio):
        self._sensorType = "TEMP"
        self._sensorAddress = sensorAddress
        self._gpio = gpio

    # variable assignment methods for correct implementation
    @property
    def sensorType(self):
        return "TEMP"

    @sensorType.setter
    def sensorType(self, sensorType):
        self._sensorType = sensorType

   
    # get and set sensorAddress property
    @property
    def sensorAddress(self):
        return self._sensorAddress
    
    @sensorAddress.setter
    def sensorAddress(self, sensorAddress):
        self._sensorAddress = sensorAddress

    
    # Get and Set GPIO pin property
    @property
    def gpio(self):
        return self._gpio
    
    @gpio.setter
    def gpio(self, gpio):
         self._gpio = gpio
    


    # returns measurement
    def getMeasurement(self):
        # implement correct code: return integer value 12 for now
        return 12

    # string modifier
    def __str__(self):
        return "Type: " + self._sensorType + "\nAddress: " + self._sensorAddress + "\nGPIO: " + str(self._gpio)

