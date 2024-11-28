s="aaaabbcccddd"
u=''
for ch in s:
    if ch not in u:
        u+=ch
for ch in u:
    print(f'{ch}={s.count(ch)}')

     