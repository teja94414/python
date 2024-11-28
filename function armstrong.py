def armstrong(n,power,res=0):
    while n!=0:
        rem=n%10
        res=res+rem**power
        n//=10
    return res
num=153
print('armstrong number'if armstrong(num,len(str(num)))==num else'not armstrong number')