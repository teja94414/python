def fact(n,fact=1):
    for val in range (1,n+1):
        fact*=val
    return fact
print (fact(3))