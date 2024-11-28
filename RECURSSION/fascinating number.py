def fascinate (num,str_num,val):
    if val ==10:
        return True
    if str(val)not in str_num:
        return False
    return fascinate (num,str_num,val+1)
n=int(input())
str_num=str(n*1)+str(n*2)+str(n*3)
print'fascinate number'if fascinate (num,str_num,val else'not fascinate number')
