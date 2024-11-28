def linear(l,target):
    for ind in range(len(l)):
        if l[ind]==target:
            return ind
    return-1
l=[5,3,8,2,6,1,8]
target=8
print(linear(l,target))

