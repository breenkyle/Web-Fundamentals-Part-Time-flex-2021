from dessert import Dessert

class Pie(Dessert):
    def __init__(self, name, ingrediants, season, quantity):
        super().__init__(name, ingrediants, season, quantity)

    def topping(self):
        return "Ice Cream"

    def amount(self):
        return "Needs Box"

class Pastry(Dessert):
    def __init__(self, name, ingrediants, season, quantity):
        super().__init__(name, ingrediants, season, quantity)

    def topping(self):
        return "Whipped Cream"


class Cupcake(Dessert):
    def __init__(self, name, ingrediants, season, quantity):
        super().__init__(name, ingrediants, season, quantity)

    def topping(self):
        return "Butter Cream"

apple_pie = Pie("Apple Pie", "Apples", "Fall", 1)
print(apple_pie.amount())
print(apple_pie.topping())
canoli = Pastry("Canoli", "Canoli", "4 Season", 12)
print(canoli.name)

red_velvet = Cupcake("Red Velvet", "Deliciousiness", "4 Season", 24)
print(red_velvet.amount())