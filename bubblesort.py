def bubblesort(list):

# Swap the elements to arrange in order
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j]>l[j+1]:
                temp = l[j]
                list[j] = list[j+1]
                list[j+1] = temp
    print(list)

l = [19,2,31,45,6,11,121,27]
bubblesort(list)
