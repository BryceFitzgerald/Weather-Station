import LLNode
class LLQueue:

	# template for Measurement Queue provided by Geeks for geeks
	# original source code: https://www.geeksforgeeks.org/queue-linked-list-implementation/
    def __init__(self):
        self.front = None
        self.back = None
        self.length = 0

    # if queue is empty, return true
    def isEmpty(self):
        return self.front == None
    
    # increment length variable 
    def increment(self):
    	self.length += 1
    
    # decrement length variable
    def decrement(self):
        self.length -= 1

    # add item to the queue
    def EnQueue(self, item):
        temp = LLNode.LLNode(item)

        if self.back == None:
            self.front = temp
            self.back = temp

        self.increment()
        self.back.next = temp
        self.back = temp
    # remove item to the queue
    def DeQueue(self):
        # if the queue is empty, return 
        if self.isEmpty():
            return

        # set temp to front
        temp = self.front
        # set front to next
        self.front = temp.next

        # if front is empty, set back to empty
        if(self.front == None):
            self.back = None
            # set length variable to 1 (later to be transformed to 0)
            self.length = 1

        # decrement length variable
        self.decrement()
       
        # return measurement
        return temp.data

    








    
    