def l(lcm,n1,n2):
    if lcm%n1==0 and lcm%n2==0:
        return lcm
    return l(lcm+1,n1,n2)
num1=int(input())
num2=int(input())
print(l('num1' if num1>num2 else 'num2',num1,num2)) 