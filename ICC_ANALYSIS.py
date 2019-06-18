def find_matches(country_name):
    res=[]
    
    for i in match_list:
        temp=i.split(":")
        if temp[0]==country_name:
            res.append(i)
    return(res)        

def max_wins():
    result={}
    u=[]
    for i in match_list:
        temp=i.split(':')
        if temp[1] not in u:
            u.append(temp[1])
            result.update({temp[1]:[]})
    for j in result.keys():
        
        t=[]
        r=0
        maxx=0
        for i in match_list:
            temp=i.split(":")
            
            if temp[1]==j:
                if int(temp[-1])>maxx:
                    while len(result[j])>0:
                        result[j].pop()
                    result[j].append(temp[0])
                    maxx=int(temp[-1])
                elif int(temp[-1])==maxx:
                    result[j].append(temp[0])
                    maxx=int(temp[-1])
                 
    return(result)    

def find_winner(country1,country2):
    #Remove pass and write your logic here
    e=[0,0]
    for i in match_list:
        temp=i.split(":")
        if temp[0]==country1:
            e[0]+=int(temp[-1])
        elif temp[0]==country2:
            e[1]+=int(temp[-1])
    if e[0]>e[1]:
        return(country1)
    elif e[1]>e[0]:
        return(country2)
    else:
        return("Tie")

match_list=["AUS:CHAM:5:2","AUS:WOR:2:1","ENG:WOR:2:0","IND:T20:5:3","IND:WOR:2:1","PAK:WOR:2:1","PAK:T20:5:1","SA:WOR:2:0","SA:CHAM:5:1","SA:T20:5:0"]

print("The match status list details are:")
print(match_list)
print(max_wins())
print(find_matches("PAK"))
print(find_winner("IND","AUS"))
