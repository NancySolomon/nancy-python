
#Finding the elements in an array with the given sum
def pairsum(l,sum):
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if l[i]+l[j]==sum:
                print(l[i],l[j])
                break
       break
print("pair not found")
l=list(map(int,input().split()))
sum=int(input())
pairsum(l,sum)