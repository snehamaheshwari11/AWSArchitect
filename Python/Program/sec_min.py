def sec_min(l):
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j]>l[j+1]:
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp
    return l[1]

print(sec_min([12,15,10,13,18,90,8,2,90,6,4]))
            