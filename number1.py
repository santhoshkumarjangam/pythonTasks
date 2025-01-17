import math

class Arthmetic:

    def __init__(self,value):
        self.value = value

    def ChkPrime(self):
        count = 0

        for i in range(2,int(math.sqrt(self.value))+1):
            if self.value % i == 0:
                count += 1
                break
        if count == 0:
            return True
        else:
            return False
            

    def ChkPerfect(self):
        sum = self.SumFactors()
        if sum == self.value:
            return True
        else:
            return False

    def SumFactors(self):
        return sum(self.Factors())

    def Factors(self):
        factors=[]
        for i in range(1,self.value):
            if self.value % i == 0:
                factors.append(i)

        return factors
    

number = Arthmetic(6)
print(f"Is prime?: {number.ChkPrime()}")
print(f"Is perfect?: {number.ChkPerfect()}")
print(f"Sum of factors: {number.SumFactors()}")