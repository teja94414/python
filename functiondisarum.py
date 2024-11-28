def disarum (n,power,res=0):
    while n!=0:
        rem=n%10
        res=res+rem**power
        n//=10
        power=power-1
    return res
num=135
print('disarum number'if disarum (num,len(str(num)))==num else'not disarum number')