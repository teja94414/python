def dig_sum (num,ans=0):
    while num!=0:
        rem=num%10
        ans=ans+rem
        num=num//10
    return ans
num=3456
print(dig_sum(num))