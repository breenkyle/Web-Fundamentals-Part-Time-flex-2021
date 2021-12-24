# pie_one = {'name': 'Apple Pie', 'Topping' : 'Ice Cream', 'season_availability' : 'fall'}
# pie_two = {'name': 'Cherry Pie', 'Topping' : 'Whipped Cream', 'season_availability' : 'spring'}
# pie_three = {'name': 'Pumpkin', 'Topping' : 'Ready Whip', 'season_availability' : 'fall'}

# pie_four = {'name': 'Pumpkin', 'Topping' : 'Ready Whip', 'seasonavailability' : 'fall'}


# Blueprint
class Pie:

    def __init__(self, name, crust, price, topping = "cheese", size = 'personal'):
        self.name = name
        self.topping = topping
        self.crust = crust
        self.price = price
        self.size = size

    def addTopping(self, topping):
        self.topping = topping
        return self

    def addSide(self, side):
        self.side = side
        return self


# pie_one = Pie("Pizza Pie", "Cheese", "Thin", 10, "Personal")
# print(pie_one.topping)

# pie_one.addTopping("Sausage")
# print(pie_one.topping)

# pie_two = Pie("Sheppards Pie", "Thick", 10, "Potatoes", 'Large')
# pie_two.addSide("Buffalo Wings")
# print(pie_two.side)

pie_three = Pie("Sweet Potato Pie", "Thick", 15)
print(pie_three.name)

pie_three.addTopping("Marshmellows").addTopping("Brown Sugar").addSide("Bacon")

print(pie_three.topping)
print(pie_three.side)

# print(pie_two.size)
# print(pie_two.topping)