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
    

