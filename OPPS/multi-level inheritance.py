class parent:
    var1=40
    var2=80
class child1(parent):
    var3=30
    var2=100
class child2(parent):
    var3=40
    var4=10
    
obj=child2()
print(obj.var2)
    
