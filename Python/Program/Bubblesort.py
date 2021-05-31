def bubble(l):
    temp=0
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j]>l[j+1]:
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp
    return l


def zigzag(l):
    ll=[]
    last_index=len(l)-1
    loop_to_run=int(len(l)/2)
    i=0
    print(loop_to_run, len(l))
    while i<loop_to_run:
        ll.append(l[i])
        ll.append(l[last_index])
        i+=1
        last_index-=1
    if len(l)%2==1:
        ll.append(l[loop_to_run])
    return ll

print(zigzag(bubble([11,3,5,7,9,11,13,15,17])))