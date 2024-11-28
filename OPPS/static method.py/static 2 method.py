class laptop:
    name ="hp"
    
    def __init__ (self,version,processor,model,price):
        self.version=version
        self.processor=processor
        self.model=model
        self.price=price
    @staticmethod
    def display():
        print("static method is indepenedent of self and cls")
l1=laptop('i7','intel','razon',60000)
laptop.display()
l1.display()