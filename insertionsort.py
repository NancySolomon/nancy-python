def insertsort(l):
    for i in range(1,len(l)):
        j=i-1
        nxtele=l[i]
        while l[j]>nxtele and j>=0:
            l[j+1]=l[j]
            j=j-1
        l[j+1]=nxtele
    return l
l=[19,2,31,45,30,11,121,27]
print(insertsort(l))

