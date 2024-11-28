left=[1,3,5,7]
right=[2,4,6,6]
L=[0]*(len(left)+len(right))
li,ri,ind=0,0,0
while li<len(left)and ri<len(right):
    if left[li]>right[ri]:
        L[ind]=right[ri]
        ri+=1
    else:
        L[ind]=left[li]
        li+=1
    ind +=1
while li < len(left):
    L[ind]=left[li]
    li +=1
    ind+=1
while ri <len(right):
    L[ind]=right[ri]
    ri +=1
    ind +=1
print(L)
    
