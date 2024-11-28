def factorial (rem):
    if rem==0 or rem==1:
        return 1
    return rem * factorial(rem-1)
def strong (digits):
    if digits ==0:
        return 0
    return factorial (digits%10)+strong(digits//10)
num=145
print('strong number'if strong (num)==num else'not strong number')