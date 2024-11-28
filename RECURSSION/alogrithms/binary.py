l=[-7,-2,3,5,11,19,26,36]
target=26
low=0
high=len(l)-1
while low<=high:
    mid=(low+high)//2
    if l[mid]>target:
        high=mid-1
    elif l[mid]<target:
        low=mid+1
    elif l[mid]==target:
        print(mid)
        break
else:
    print(-1)
    
        
    
    
    