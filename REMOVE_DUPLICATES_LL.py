#DSA-Assgn-7
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


    def display(self):
        temp=self.__head
        while(temp is not None):
            print(temp.get_data())
            temp=temp.get_next()
    def __str__(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
            msg.append(str(temp.get_data()))
            temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return msg
def remove_duplicates(duplicate_list):
    temp=duplicate_list.get_head()
    while temp!=None:
        temp1=temp.get_next()
        while temp1!=None:
            if temp.get_data()==temp1.get_data():
                temp.set_next(temp1.get_next())
            temp1=temp1.get_next()
        
        temp=temp.get_next()    
    return duplicate_list

duplicate_list=LinkedList()
duplicate_list.add(32)
duplicate_list.add(42)
duplicate_list.add(42)
duplicate_list.add(42)
duplicate_list.add(44)
duplicate_list.add(44)
duplicate_list.add(44)
duplicate_list.add(44)
print(remove_duplicates(duplicate_list))

                                                    
