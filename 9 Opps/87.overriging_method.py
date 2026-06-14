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
    
            