l=[4,2,3,2]
target=5
def linear(l,target,ind=0):
    if l[ind]==len(l):
        return -1
    return(l,target,ind)
print(linear(l,target))

    