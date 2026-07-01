class calculater():
    
    def __init__(self):
        self.x = 0
        self.y = 0
        
    def get_input(self):
        self.x = int(input("Enter Value of x : "))
        self.y = int(input("Enter Value of y : "))
        return
    
    def y_input(self):
        self.y = int(input("Enter Value of y : "))
        return
    
    def addition(self):
        sum = self.x + self.y
        return sum
    
    