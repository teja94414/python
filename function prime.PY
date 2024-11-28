def prime (num):
    for den in range(2,num//2+1):
        if num % den==0:
            return 'not prime'
    return 'prime'
print(prime(11))