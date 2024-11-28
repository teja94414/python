def square (value):
    if value==0:
        return 0
    return(value%10)**2+square(value//10)
def happy(num):
    if num<=10:
        return num==1 or num==7
    return happy (square(num))
num=13
print('happy number'if happy (num)==num else'not happy number')
    