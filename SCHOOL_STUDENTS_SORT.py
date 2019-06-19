
def order_heights(student_list,height_list):
    def find_min(lst,a):
        indx=0
        minn=lst[a]
        for i in range(a,len(lst)):
            if lst[i]<=minn:
                minn=lst[i]
                indx=i
        return(indx)
    def swap(lst,a,b):
        t=lst[a]
        lst[a]=lst[b]
        lst[b]=t
    for i in range(len(height_list)):
        indx=find_min(height_list,i)
        swap(height_list,i,indx)
        swap(student_list,i,indx)
    return[student_list,height_list]

student_list=["Santa","Tris","Arun","Rachel","John"]
height_list=[132.7,129.2,135,130.6,140]
print("Initial student details :")
print("The students:",student_list)
print("Their heights:",height_list)
print()
result=order_heights(student_list,height_list)
print("After arranging the students in the order of their height:")
print("The students :",result[0])
print("Their heights:",result[1])
