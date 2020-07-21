def mergesort(l):
    if len(l)<=1:
        return l
    else:
        mid=len(l)//2
        left_list=l[:mid]
        right_list=l[mid:]
    left_list=mergesort(left_list)
    right_list=mergesort(right_list)
    return(list(merge(left_list,right_list)))
def merge(left_list,right_list):
    res=[]
    while len(left_list)!=0 and len(right_list)!=0:
         if left_list[0]<right_list[0]:
             res.append(left_list[0])
             left_list.remove(left_list[0])
         else:
            res.append(right_list[0])
            right_list.remove(right_list[0])
    if len(left_list)==0:
        res=res+right_list
    else:
        res=res+left_list
    return res
l=[8,7,4,2,-3,-4,12]
print(mergesort(l))