import Measurement

class MeasurementLLNode:
    def __init__(self, next=None, data):
        self.next = next
        self.data = data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next
    
    def setData(self, data):
        self.data = data

    def getData(self):
        return data

    