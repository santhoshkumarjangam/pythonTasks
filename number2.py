class Arthmetic:

    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self,value1,value2):
        self.value1 = value1
        self.value2 = value2

    def Addition(self):
        return self.value1 + self.value2
    
    def Subtraction(self):
        return self.value1 - self.value2
    
    def Multiplication(self):
        return self.value1 * self.value2
    
    def Division(self):
        return self.value1 / self.value2

obj1 = Arthmetic()
obj1.Accept(10,5)
print(f"Addition: {obj1.Addition()}")
print(f"Subtraction: {obj1.Subtraction()}")  
print(f"Multiplication: {obj1.Multiplication()}")  
print(f"Division: {obj1.Division()}")
