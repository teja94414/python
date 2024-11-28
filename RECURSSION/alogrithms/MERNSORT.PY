L=[1,420,3,4,100,7,18,8]
def divide(L):
    if len(L)>1:
        mid =len(L)//2
        left=L[:mid]
        rigth=L[mid:]
        print(left,rigth)
        divide(left),divide(rigth)
        conq(L,left,rigth)
def conq(L,left,right):
    li,ri,ind=0,0,0
while li <len(left)and ri<len(right):
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
divide(L)
print(L)
    
