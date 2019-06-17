import random
def find_it(num,element_list):
    
    c=0
    for i in element_list:
        c+=1
        if i==num:
            break
    
    return(c)
        
def initialize_list_of_elements(n):
    list_of_elements=[]
    for i in range(1,n+1):
        list_of_elements.append(i)
    mid=n//2
    for j in range(0,n):
        index1=random.randrange(0,mid)
        index2=random.randrange(mid,n)
        num1=list_of_elements[index1]
        list_of_elements[index1]=list_of_elements[index2]
        list_of_elements[index2]=num1
    return list_of_elements

def play(n):
    element_list=initialize_list_of_elements(n)
    num=random.randrange(n)
    guesses=find_it(num,element_list)
    print(guesses)
        

play(400)
