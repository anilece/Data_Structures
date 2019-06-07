class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None

    def get_data(self):
        return self.__data
    
    def set_data(self,data):
        self.__data=data
    
    def get_next(self):
        return self.__next
    
    def set_next(self,next_node):
        self.__next=next_node
    def __str__(self):
        return(self.__data)
class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
    
    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
    def add(self,data):
        t=Node(data)
        if self.__head==None:
            self.__head=self.__tail=t
        else:
            self.__tail.set_next(t)
            t.set_next(None)
            self.__tail=t
        
    
    def display(self):
        temp=self.__head
        while temp!=None:
            print(temp.get_data(),end='')
            if temp.get_next()!=None:
                print("--",end='')
                
            temp=temp.get_next()
        print()    
        
    
    def find_node(self,data):
        f=0
        temp=self.__head
        while temp!=None:
            if temp.get_data()==data:
                f=1
                return(temp)
            temp=temp.get_next()    
        if f==0:
            return(None)
    def __str__(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
           msg.append(str(temp.get_data()))
           temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return msg


list1=LinkedList()
list1.add("sugar")
list1.add("Sugar")
list1.add("Sugar")
list1.add("Sugar")
list1.display()
print(list1)
node=list1.find_node("Sugar")
if(node!=None):
    print("Node found",node)
else:
    print("Node not found") 
