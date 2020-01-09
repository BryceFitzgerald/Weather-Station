import LLNode
class MeasurementQueue:

	# template for Measurement Queue provided by Geeks for geeks
	# original source code: https://www.geeksforgeeks.org/queue-linked-list-implementation/
    def __init__(self):
        self._front = None
        self._back = None
        self._length = 0

    # if queue is empty, return true
    def isEmpty(self):
        return self._front == None
    
    # increment length variable 
    def increment(self):
    	self._length += 1
    
    # decrement length variable
    def decrement(self):
        self._length -= 1

    # add item to the queue
    def EnQueue(self, item):
        temp = LLNode(item)

        if self.rear == None:
            self.front = temp
            self.rear = temp
        increment()

    # remove item to the queue
    def DeQueue(self):
        # if the queue is empty, return 
        if self.isEmpty():
            return

        # set temp to front
        temp = self.front
        # set front to next
        self.front = temp.next

        # if front is empty, set rear to empty
        if(self.front == None):
            self.rear = None
            # set length variable to 1 (later to be transformed to 0)
            self._length = 1

        # decrement length variable
        decrement()
       
        # return measurement
        return temp.getData()

    








    
    