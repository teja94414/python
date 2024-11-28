s="hello"
print({s[ind]:s[0:len(s)-ind] for ind in range(0,len(s)) })