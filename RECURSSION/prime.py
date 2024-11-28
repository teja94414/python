def prime(fv,half,num):
    if fv==half+1:
        return True
    if num%fv==0:
        return False
    return prime(fv +1,half,num)
num=5
fv=2
half=num//2
print('prime'if prime(fv,half,num)else'not prime')