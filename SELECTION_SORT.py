
def swap(num_list, first_index, second_index):
    t=num_list[first_index]
    num_list[first_index]=num_list[second_index]
    num_list[second_index]=t


def find_next_min(num_list,start_index):
    minn=num_list[start_index]
    e=0
    for i in range(start_index,len(num_list)):
        if num_list[i]<=minn:
            minn=num_list[i]
            e=i
    return(e)
def selection_sort(num_list):
    for i in range(len(num_list)):
        temp=find_next_min(num_list,i)
        swap(num_list,i,temp)


num_list=[8,2,19,34,23, 67, 91]
print("Before sorting;",num_list)
selection_sort(num_list)
print("After sorting:",num_list)
