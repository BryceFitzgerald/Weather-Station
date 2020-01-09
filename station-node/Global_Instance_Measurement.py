

class Global_Instance_Measurement:
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

    

    def toString(self):
    	returnString = "Recorded: " + str(getLogDate) +"\nTemperature: " + str(tempMeasurement) + "\nPressure: " + str(pressureMeassurement) +"\n"