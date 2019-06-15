class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0
    
    def get_max_size(self):
        return self.__max_size
    
    def is_full(self):
        if self.__rear==self.__max_size-1:
            return(True)
        return(False)
    def enqueue(self,data):
        if self.is_full():
            print(" Queue is full")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data
    def is_empty(self):
        if self.__front>self.__rear:
            return(True)
        else:
            return(False)
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            w=self.__elements[self.__front]
            self.__front+=1
            
            return(w)
    def display(self):
        e=self.__front
        if e<=self.__rear:
            while e<=self.__rear:
                print(self.__elements[e])
                e+=1
        else:
            print("empty queue")
                                              
    def __str__(self):
        msg=[]
        index=self.__front
        while(index<=self.__rear):
            msg.append((str)(self.__elements[index]))
            index+=1
        msg=" ".join(msg)
        msg="Queue data(Front to Rear): "+msg
        return msg

queue1=Queue(5)
queue1.enqueue("a")
queue1.enqueue("b")
queue1.enqueue("c")
queue1.enqueue("d")
queue1.enqueue("e")
print(queue1)

data=queue1.dequeue()
print(data)
print(queue1)
data=queue1.dequeue()
print(data)
print(queue1)
data=queue1.dequeue()
print(data)
print(queue1)
data=queue1.dequeue()
print(data)
print(queue1)
data=queue1.dequeue()
print(data)
print(queue1)
queue1.display()
data=queue1.dequeue()
data=queue1.dequeue()
print(queue1)
