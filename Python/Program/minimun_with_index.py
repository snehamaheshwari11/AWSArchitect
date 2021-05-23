
def get_min_index(l):
    min=l[0]
    index_min=0
    for index,value in enumerate(l):
        if min>value:
            min=value
            index_min=index
    return "Min Value is " + str(min), "Min Value index is "+str(index_min)

print(get_min_index([11,12,44,5,70]))
