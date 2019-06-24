def make_change(denomination_list, amount):
    if amount in denomination_list:
        return (1)
    else:
        d=denomination_list
        d.sort(reverse=True)
        a=[]
        for i in d:
            if i <=amount :
                n=amount//i
                amount=amount%i
                for j in range(0,n):
                    a.append(i)
        print(a) 
        if len(a)>0:
            return(len(a))
        else:
            return(-1)

amount= 20
denomination_list = [1,15,10]
make_change(denomination_list, amount)
