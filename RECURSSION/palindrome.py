def reverse(num,pos):
    if num==0:
        return pos
    return reverse(num//10,pos*10+(num%10))
num=151
print('palindrome')