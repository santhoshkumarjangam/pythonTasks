class Circle:
    PIE = 3.14

    def __init__(self):
        self.radius = 0.0

    def Accept(self,radius):
        self.radius = radius

    def CalculateArea(self):
        self.area = Circle.PIE*(self.radius**2)

    def CalculateCircumference(self):
        self.circumference = 2*Circle.PIE*self.radius

    def Display(self):
        print(f"Radius: {self.radius}")
        print(f"Area: {self.area}")
        print(f"Circumferene: {self.circumference:.2f}")


c1 = Circle()
c1.Accept(10)
c1.CalculateArea()
c1.CalculateCircumference()
c1.Display()

