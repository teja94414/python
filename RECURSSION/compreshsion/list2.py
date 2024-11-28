s='abcd'
print({s[ch]:s[ch]*ch for ch in range(1,len(s))})