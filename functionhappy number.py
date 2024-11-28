def sq(num,res=0):
    while num!=0:
        rem=num%10
        res+=rem**2
        num//=10
    return res
def happy (dig):
    while dig>9:
        dig=sq(dig) 
    return dig
num=20
var=happy (num)
print('happy number'if var==1 or var==7 else'not happy number')

        
        