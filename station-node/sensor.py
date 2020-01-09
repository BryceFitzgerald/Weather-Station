# import abstract class libraries (ABC = abstact parent class, abstractmethod = method decorator)
import abc
from abc import ABC, abstractmethod


# Abstract Sensor Class
class Sensor(ABC):

    # getMeasurement; abstract method: returns measurement
    def getMeasurement(self):
        # Secret sauce is secret and is dependent on Sensor Used
        pass

    def __str__(self):
        # toString method
        pass
    
    # abstract property: enforce varaible assignment in sublcasses
    @abc.abstractproperty 
    def sensorType(self):    # returns sensor type : String
        pass

    @abc.abstractproperty
    def sensorAddress(self): # returns sensorAddress: String
        pass
    
    @abc.abstractproperty
    def gpio(self):          # returns gpio: int
        pass
    

class TemperatureSensor(Sensor):
    def __init__(self, sensorAddress, gpio):
        self._sensorType = "TEMP"
        self._sensorAddress = sensorAddress
        self._gpio = gpio

    # variable assignment methods for correct implementation
    @property
    def sensorType(self):
        return "TEMP"

    @sensorType.setter
    def setter(self, sensorType):
        self._sensorType = sensorType


    @property
    def sensorAddress(self):
        return self._sensorAddress
    
    @sensorAddress.setter
    def sensorAddress(self, sensorAddress):
        self._sensorAddress = sensorAddress


    @property
    def gpio(self):
        return self._gpio
    
    @gpio.setter
    def gpio(self, gpio):
         self._gpio = gpio
    


    # returns measurement
    def getMeasurement(self):
        # implement correct code
        return 12

    # string modifier
    def __str__(self):
        return "Type: " + self.sensorType + "\nAddress: " + self.sensorAddress + "\nGPIO: " + str(self.gpio)

def Main():
    ts1 = TemperatureSensor("t0123", 12)
    print(str(ts1))
if __name__ == '__main__':
    Main()