class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None

    def printlist(self):
        temp=self.head
        while(temp!=None):
            print("linked list is  ",end='')
            print(temp.data,"==>",end='')
            temp=temp.next
        print("None")    
    def deletion(self):
        temp=self.head
        self.head=self.head.next
        temp.next=None

    def Insertion(self,data):
        self.data=data
        temp=Node(data)
        temp.next=self.head
        self.head=temp
obj=SLL()
print("linked list implementation","1.Insertion at begining","2.Deletion at begining","3.print linked list")
ch=0
while(ch!=4):
    ch=int(input())
    if(ch==1):
        print("Enter the value to be inserted")
        data=input()
        obj.Insertion(data)
        obj.printlist()
    elif (ch==2):
        obj.deletion()
        obj.printlist()
    elif (ch==3):
        obj.printlist()
        
