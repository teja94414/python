s="happy"
for sv in range (len(s)):
    for ev in range (sv+1,len(s)+1):
        res=''
        for ind in range (sv,ev):
            res+=s[ind]
            print(res)