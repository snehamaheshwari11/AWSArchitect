def max_num(l):
    max=l[0]
    index_max=0
    for index, value in enumerate(l):
        if max<value:
            max=value
            index_max=index
    return "Max number is "+ str(max) +" and max number index is "+ str(index_max)

print(max_num([101,1900,3,12,31,42,2,99]))
