class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1

    def get_max_size(self):
        return self.__max_size

    def is_full(self):
        if self.__top==self.__max_size:
            print("stack is full")
            return(True)
        else:
            return(False)
       
    def push(self,data):
        self.__top+=1
        if self.is_full() is not True:
            
            self.__elements[self.__top]=data
        else:
            print(data,"unale to push")
            
                                          
    def __str__(self):
        msg=[]
        index=self.__top-1
        while(index>=0):
            msg.append((str)(self.__elements[index]))
            index-=1
        msg=" ".join(msg)
        msg="Stack data(Top to Bottom): "+msg
        return msg

stack1=Stack(5)
stack1.push("Shirt1")
stack1.push("Shirt2")
stack1.push("Shirt3")
stack1.push("Shirt4")
stack1.push("Shirt5")
stack1.push("Shirt6")
print(stack1)
