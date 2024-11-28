s="abcd"
print([s[sv:ev]for sv in range(len(s)) for ev in range(sv+1,len(s)+1)])
