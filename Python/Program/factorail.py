def fact(num):
    i=1
    ans=1
    while i<=num:
        ans=ans*i
        i+=1
    return ans

print(fact(10))