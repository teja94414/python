def factorial (num,fact=1):
    for val in  range(2,num+1):
        fact*=val
    return fact

def armstrong(n,res=0):
    power=len(str(n))
    res=0
    dup=n
    while n!=0:
        rem=n%10
        res=res+rem**power
        n=n//10
    if dup==res:
        return armstrong
    return not armstrong
n=153
print(armstrong(n))