def swap(i,j,l):
    temp=l[i]
    l[i]=l[j]
    l[j]=temp


def zigzag(l):
    end=len(l)
    i=0
    while i< (end-1):
        if i%2==0:
            # greate compar
            if l[i]>l[i+1]:
                swap(i,i+1,l)
        else:
            # less comparsion    
            if l[i] < l[i+1]:
                swap(i,i+i,l)
        i+=1
    print(l)

zigzag([11,11,2,3,4,5,6,7,8])