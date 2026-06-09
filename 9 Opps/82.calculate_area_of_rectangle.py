# Calculate area of rectangle
class Rectangle():
    
    def __init__(self,length,breath):
        self.length = length
        self.breath = breath
        
    def area(self):
        return f"Area of Rectagle {self.length*self.breath}"

rectangle1 = Rectangle(2,4)
rectangle2 = Rectangle(37,654)

print(rectangle1.area())
print(rectangle2.area())