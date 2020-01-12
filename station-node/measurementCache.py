import temperatureSensor
import pressureSensor
import LLQueue
import measurement

class measurementCache:
    def __init__(self, temperatureSensor, pressureSensor):
        self.temperatureSensor = temperatureSensor
        self.pressureSensor = pressureSensor
        self.queue = LLQueue.LLQueue()
        self.length = 0

    def updateCache():
        measurement = measurement(temperatureSensor, pressureSensor)
        self.queue.EnQueue(measurement)
        self.length = self.length + 1

    def pull():
        self.length = self.length - 1
        return self.queue.DeQueue()

    def printCache():
        # create temporaryCache
        temporaryQueue = LLQueue.LLQueue()
        # copy and print primary cache item into temporary cache
        for item in range(self.length()):
            placeholder = self.queue.DeQueue()
            print(str(placeholder))
            temporaryQueue.EnQueue(placeholder)
        
        # reassign temporaryCache to primary cache
        self.queue = temporaryQueue

    def copyCache():
        return self.queue




    	
        