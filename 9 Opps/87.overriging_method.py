class Animal():
    
    def __init__(self,animal_name,species,age,gender):
        self.animal_name = animal_name
        self.species = species
        self.age = age
        self.gender = gender
        self.food = "Unknow"
        
    def eat(self):
        user_input = input(f"Enter habitat for {self.animal_name} (Forest,Water,Home): ":).lower()
        if user_input == ("forest","F","f"):
            self.food = "Grass", "Meat"
        elif user_input == ("W","w","water"):
            self.food = "fish"
        elif user_input == ("home","h","H"):
            self.food = "Pet Food"
        else:
            self.food = "Anithing"
        return
    
    def speak(self):
        return f"Animal Speak."
    
    def sleep(self):
        return f"Animal is sleeping."
    
    def animal_details(self):
        return f"""
    
    Animal Name : {self.animal_name}
    Animal Species : {self.species}
    Animal Age : {self.age}
    Animal Gender : {self.gender}
    Animal Eat : {self.eat()}
    Animal Sleep : {self.sleep()}
    Animal Speak : {self.speak()}
    
    """
class dog(Animal):
    
    def __init__(self,name,species,age,gender):
        super().__init__(name,species,age,gender)
        
    def speak(self):
        parent_sound = super().speak()
        return f"Barking: Woof Woof!"
    
    def animal_details(self):
        all = super().animal_details()
        return all

            