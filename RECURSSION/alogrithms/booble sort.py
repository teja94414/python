L=[20,10,40,70,-10]
for ind1 in range (len(L)-1):
    for ind2 in range(len(L)-1-ind1):
        if L[ind2+1]>L[ind2+1]:
            L[ind2+1],[ind2+1],L[ind2]=L[ind2+1],L[ind2]
print(L)