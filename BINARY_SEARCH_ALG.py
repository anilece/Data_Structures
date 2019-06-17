import random
def find_it(num,element_list):
    #l=low h=high m=middle
    l=0
    h=len(element_list)
    c=0
    for i in range(l,h):
        m=(l+h)//2
        print(m,l,h)
        c+=1
        if m==num:
            break
        elif m>num:
            h=m-1
            l=l
        elif m<num:
            l=m+1
            h=h
        
    return(c)
    
def initialize_list_of_elements(n):
    list_of_elements=[]
    for i in range(1, n+1):
        list_of_elements.append(i)
    return list_of_elements

def play(n):
    element_list=initialize_list_of_elements(n)
    num=random.randrange(n)
    guesses=find_it(num,element_list)
    print(num,guesses)


play(400)
