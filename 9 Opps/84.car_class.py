class car():
    
    def __init__(self,brand,model,fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
        self.__speed = 0
        self.is_start = False
    
    def start_engine(self):
        if self.is_start == True:
            # print("Car is allready Start.")
            return True
        
        else:
            self.is_start = True
            # print("Car is Start.")
            return True