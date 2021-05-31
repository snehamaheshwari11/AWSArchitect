def bubble(l):
    temp=0
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j]>l[j+1]:
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp
    return l

print(bubble([1,10,12,3,9,2]))