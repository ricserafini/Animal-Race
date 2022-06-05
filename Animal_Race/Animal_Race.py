from random import randint

class Animal:
    
    def __init__(self, name):
        self.name = name
        self.current_position = 0
    
    def get_name(self):
        animal_name = f"{self.name}"
        return animal_name.title()
    
class Turtle(Animal):
    
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.current_position = 0
            
class Race:
    
    def __init__(self):
    
        self.members = []
        self.race_lenght = 1000
        self.ranking =[]
        
    def add_turtle(self, partecipant: Turtle):
        
        self.members.append(partecipant)
    
    def add_animal(self, partecipant: Animal):
        
        self.members.append(partecipant)
        
    def show_partecipants(self):
        
        for member in self.members:
            print(member.name)
          
    def start_race(self):
    
        while len(self.members) > 0: 
        
            for member in self.members:
            
                movement = randint(5, 15)
            
                member.current_position += movement
            
                if member.current_position < 1000:
                    print(member.current_position, member.name)
                
                elif member.current_position >= 1000:
                    self.members.remove(member)
                    self.ranking.append(member)
                    print(f"{member.name} is arrived!")
            
    def show_ranking(self):
        for idx, member in enumerate(self.ranking):
        
            print(idx+1, member.name)
    
    
my_race = Race()

my_turtle1 = Turtle('Geppa')
my_turtle2 = Turtle('Franca') 
my_turtle3 = Turtle('Carla')
my_turtle4 = Turtle('Peppa')
my_turtle5 = Turtle('Puffa')
my_dog1 = Animal('Rocco')
my_dog2 = Animal('Rebecca')
my_cat1 = Animal('Pipino')

my_race.add_turtle(my_turtle1)
my_race.add_turtle(my_turtle2)
my_race.add_turtle(my_turtle3)
my_race.add_turtle(my_turtle4)
my_race.add_turtle(my_turtle5)
my_race.add_animal(my_dog1)
my_race.add_animal(my_dog2)
my_race.add_animal(my_cat1)

my_race.show_partecipants()
my_race.start_race()
my_race.show_ranking()
