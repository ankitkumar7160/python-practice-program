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
    
    def accelerate_car(self,increase):
        if self.is_start == False:
            print("Oops! Engine OFF.")
            user = input("Do you want to Start Engine? yes/no: ").lower()
            if user == "yes":
                self.start_engine = self.start_engine()
            else:
                return False
            
        self.__speed = self.__speed + increase