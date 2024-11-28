def factorial (n,fact=1):
    for val in range (1,n+1):
        fact*=val
def strong (num,res=0):
    while num!=0:
        rem=num%10
        res+=fact(rem)
        num//=10
    return res
num=145
print('strong'if strong(num)==num else'not strong')