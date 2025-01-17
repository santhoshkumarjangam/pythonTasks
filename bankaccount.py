class BankAccount:

    ROI = 10.5

    def __init__(self,name,amount):
        self.Name = name 
        self.Amount = amount

    def deposit(self,amount):
        self.Amount += amount
        print(f"Deposited {amount}")
        print(f"Available balance is: {self.Amount}")

    def withdraw(self,amount):
        if amount > self.Amount:
            print("Insufficient balance")
        else:    
            self.Amount -= amount
            print(f"Withdrawed {amount}")
        print(f"Available balance is: {self.Amount}")

    def calculateInterest(self):
        self.interest = (self.Amount * BankAccount.ROI) / 100
        print(f"Interest is {self.interest}")
    

    def display(self):
        print("Account Details:")
        print(f"Name: {self.Name}")
        print(f"Amount: {self.Amount}")

b1 = BankAccount("Santhosh Kumar",1000000)
b1.deposit(100000)
b1.withdraw(50000)
b1.calculateInterest()
b1.display()




