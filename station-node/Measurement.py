

class Measurement:
    def __init__(self, tempMeasurement, pressureMeassurement, humidMeasurement, logDate, tempSensor, pressureSensor, humidSensor):
        # Measurement Values
        self.tempMeasurement = tempMeasurement
        self.pressureMeassurement = pressureMeassuremen

        # Date and time of measurement
        self.logDate = logDate

        # Sensor objects
        self.tempSensor = tempSensor
        self.pressureSensor = pressureSensor

    def getTempMeasurement(self):
    	return self.tempMeasurement

    def getPressureMeasurement(self):
        return self.pressureMeassurement

    def getHumidMeasurement(self):
        return self.humidMeasurement

    def getLogDate(self):
        return logDate

    def setTempMeasurement(self,tempMeasurement):
    	self.tempMeasurement = tempMeasurement

    def setPressureMeasurement(self, pressureMeassurement):
        self.pressureMeassurement = pressureMeassurement

    def getPressureSensorAddress(self):
        return self.pressureSensor.getAddress()

    def getTemperatureSensorAddress(self):
        return self.tempSensor.getAddress()

    def setSensorAddress(self, sensor):
        self.tempSensor = sensor

    def setPressureSensor(self, sensor):
        self.pressureSensor = pressureSensor
    

    def toString(self):
    	returnString = "Recorded: " + str(getLogDate) +"\nTemperature: " + str(tempMeasurement) + "\nPressure: " + str(pressureMeassurement) +"\n"
    	returnString += "Temp Address: " + tempSensor.getAddress() + "\nPressure Address: " + tempSensor.getAddress()