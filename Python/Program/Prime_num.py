def prime_num(num):
    end=int(num/2)
    i=2
    while i<=end:
        if num%i==0:
            return "Not prime"
        i+=1
    return "Prime"


print(prime_num(21))
