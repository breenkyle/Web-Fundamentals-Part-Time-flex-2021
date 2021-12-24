class Pet:
    def __init__(self, name , type , tricks, noise ):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.noise = noise
    def sleep(self):
        self.energy ++ 25 #- increases the pets energy by 25#
        return self
    def eat(self):
        self.energy += 5
        self.health += 10 #- increases the pet's energy by 5 & health by 10
        return self
    def play(self):
        self.health += 5 #- increases the pet's health by 5
        return self
    def noise(self):
            print(self.noise)


class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , Pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet #("Victory", "Cat", "Yell", 100, 50)
    def walk(self):
        self.pet.play #- walks the ninja's pet invoking the pet play() method
        return self
    def feed(self): #- feeds the ninja's pet invoking the pet eat() method
        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}!")
        else:
            print("Oh no!!! You need more pet food!")
        return self

    def bathe(self):
        self.pet.noise
        return self #- cleans the ninja's pet invoking the pet noise() method

my_treats = [ 'Greenies', 'Tuna', 'Catnip']
my_pet_food = ["Hill's Science Diet", "Iams"]

victory = Pet("Victory", "Cat", ["Yell", "Loaf"], "YEAOOOOW")

kyle = Ninja("Kyle", "Breen", my_treats, my_pet_food, victory)

kyle.feed()
kyle.walk
kyle.bathe

