l=[10,3,9,7,-2,4]                            
    
for ind1 in range (len(l)-1):
        li=ind1
        for ind2 in range(ind1+1,len(l)):
           if l[li]>l[ind2]:
              li=ind2
        l[li],l[ind1]=l[ind1],l[li]
print(l)