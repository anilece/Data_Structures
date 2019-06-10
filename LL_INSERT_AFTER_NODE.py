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

class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
    
    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
    def add(self,data):
        temp=Node(data)
        if self.__head==None:
            self.__head=self.__tail=temp
        else:
            self.__tail.set_next(temp)
            self.__tail=temp
        #Remove pass and copy the code you had written to add an element.
    
    def display(self):
        temp=self.__head
        while temp!=None:
            if temp.get_next()!=None:
                print(temp.get_data(),"-->",end=" ")
            else:
                print(temp.get_data())
            temp=temp.get_next()
    
    def find_node(self,data):
        temp=self.__head
        f=0
        while temp!=None:
            
            if temp.get_data()==data:
                f=1
                break
            temp=temp.get_next()
        if f==1:
            return (temp)
        else:
            return(None)
    
    def insert(self,data,data_before):
        
        if self.find_node(data_before)!=None:
            temp=self.find_node(data_before)
            temp1=Node(data)
            if temp.get_next==None:
                temp.set_next(temp1)
                temp1.set_next(None)
            else:
                d=temp.get_next()
                temp.set_next(temp1)
                temp1.set_next(d)
        else:
            print("next_node not found")
            
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
list1.add("Sugar")
list1.add("Sugr")
list1.add("Sugr")
list1.add("Sgar")
list1.add("ugar")
list1.insert("NewItem","Sugar")
list1.display()
                                              
