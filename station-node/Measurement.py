import Sensor

import datetime

class Measurement:

    # instantiation Method: Reqiures temperatureSensor and PressureSensor Objects
    def __init__(self, tempSensor, pressureSensor):
        # Date and time of measurement
        self.logDate = datetime.datetime.now()

        # Sensor objects
        self.tempSensor = tempSensor
        self.pressureSensor = pressureSensor
        
        # Measurement Value Varaibles
        self.tempMeasurement = tempSensor.getMeasurement()
        self.pressureMeassurement = pressureSensor.getMeasurement()

        # Sensor ID's
        self.temperatureSensorAddress = tempSensor.sensorAddress
        self.pressureSensorAddress = pressureSensor.sensorAddress
    

    def __str__(self):
        returnString = "Recorded: " + str(self.logDate) +"\nTemperature: " + str(self.pressureMeassurement) + "\nPressure: " + str(self.pressureMeassurement) +"\n"
        returnString += "Temp Address: " + self.pressureSensorAddress + "\nPressure Address: " + self.temperatureSensorAddress
        return returnString