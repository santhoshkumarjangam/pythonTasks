class Demo:
    value = 0

    def __init__(self,val1,val2):
        self.val1 = val1
        self.val2 = val2

    def fun(self):
        print("value 1:",self.val1)
        print("value 2:",self.val2)

    def gun(self):
        print("value 1:",self.val1)
        print("value 2:",self.val2)


obj1 = Demo(15,21)
obj2 = Demo(25,31)

obj1.fun()