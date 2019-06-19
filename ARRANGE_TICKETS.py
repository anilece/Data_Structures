
def arrange_tickets(tickets_list):
    def swap(lst,a,b):
        t=lst[a]
        lst[a]=lst[b]
        lst[b]=t
    def min_Pos(lst,a):
        indx=a
        minn=int(lst[a][1:])
        for i in range(a,len(lst)):
            if int(lst[i][1:])<minn:
                minn=int(lst[i][1:])
                indx=i
        return(indx)
    for i in range(len(tickets_list)):
        indx=min_Pos(tickets_list,i)
        swap(tickets_list,i,indx)
    res=[]
    for i in range(1,21):
        temp='T'+str(i)
        if temp in tickets_list:
            res.append(temp)
        else:
            res.append('V')
    g1=res[:10]
    g2=res[10:]
    k=0
    for j in g2:
        if j=="V":
            g2.remove(j)
            
    for i in range(len(g1)):
        if g1[i]=="V":
            g1[i]=g2[k]
            g2.remove(g2[k])
            

            
    return(g1)    

tickets_list = ['T5','T7','T1','T2','T8','T15','T17','T19','T6','T12','T13']
print("Ticket ids of all the available students :")
print(tickets_list)
result=arrange_tickets(tickets_list)
print()
print("Ticket ids of the ten students in Group-1:")
print(result)
