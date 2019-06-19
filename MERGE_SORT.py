sorted_list=[]
def merge_sort(num_list):
    res=[]
    low=1
    high=len(num_list)
    if low==high:
        res=(num_list)
    else:
        mid=(low+high)//2
        left_list=num_list[:mid]
        right_list=num_list[mid:]
        res1=merge_sort(left_list)
        res2=merge_sort(right_list)
        res=merge(res1,res2)
    return(res)    
def merge(left_list,right_list):
    i=0
    j=0
    sorted_list=[]
    while (i<len(left_list) and j<len(right_list)):
        if left_list[i]<right_list[j]:
            sorted_list.append(left_list[i])
            i+=1
        elif right_list[j]<left_list[i]:
            sorted_list.append(right_list[j])
            j+=1
    while i<len(left_list):
        sorted_list.append(left_list[i])
        i+=1
    while j<len(right_list):
        sorted_list.append(right_list[j])
        j+=1
    
    return(sorted_list)

num_list=[34, 67, 8, 19, 2, 23, 91, 1]
print("Before sorting:",num_list)
sorted_list = merge_sort(num_list)
print("After sorting:",sorted_list)
