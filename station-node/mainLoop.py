from Measurement import Measurement
from sensor import TemperatureSensor

def Main():
	# s1 = "Sensor1"
	# s2 = "Sensor2"
	s3 = TemperatureSensor("a123432", 144)
	# m1 = Measurement()
	print(str(s3))

if __name__ == '__main__':
	Main()
