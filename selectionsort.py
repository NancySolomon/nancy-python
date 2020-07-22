def selectionsort(l):
    for i in range(0,len(l)):
        min=i
        for j in range(i+1,len(l)):
            if l[min]>l[j]:
                min=j
        l[i],l[min]=l[min],l[i]
        print(*l) 

l=[20,120,10,1050,2]
selectionsort(l)
print(l)
