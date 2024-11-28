l=[6,7,10,11,19,30,50,70]
target=30
low=0
high=len(l)-1
while low<=high and l[low]<=target<=l[high]:
    ind=int(low+(high-low)/(l[high]-(low))*(target-l[low]))
    if l[ind]>target:
        high=ind-1
    elif l[ind]<target:
        low=ind+1
    elif l[ind]==target:
        print(ind)
        break
else:
    print(-1)

        