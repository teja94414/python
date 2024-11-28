def reverse(val,rev=0):
    while val!=0:
        rem=val%10
        val//=10
    return rev
def prime(num): 
    for den in range( 2,num//2+1):
        if num%den==0:
            return False
    return True
num=13
dup=reverse(num)
print('emrip' if dup!=num and prime(num)and prime(dup)else'not emrip')
        
        

