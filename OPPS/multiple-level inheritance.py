class parent1:
    var1=40
    var2=80
class parent2:
    var3=40
    var2=80
    
class child1(parent2,parent1):
    var3=30
    var1=100
    
    
obj=child()
print(obj.var3)
    
