class Dessert:
    store_name = "Rob's Desserts"
    def __init__(self, name, ingrediants, season, quantity):
        self.name = name
        self.ingrediants = ingrediants
        self.season = season
        self.quantity = quantity

    def topping(self):
        return "None"

    def addSide(self, side):
        self.side = side
        return self

    def amount(self):
        if self.quantity < 6:
            return "No Box"
        elif self.quantity < 36:
            return "Needs Box"
        else:
            return "Needs Carton"

    @classmethod
    def name_change(cls, name):
        cls.store_name = name







# Pie.name_change("Rob's Pie")

# pie_one = Pie("Pizza Pie", "Cheese", "Thin", 10, "Personal")
# print(pie_one.store_name)
# # pie_one.addTopping("Sausage")
# # print(pie_one.topping)

# pie_two = Pie("Sheppards Pie", "Thick", 10, "Potatoes", 'Large')
# pie_two.addSide("Buffalo Wings")
# print(pie_two.store_name)

# pie_three = Pie("Sweet Potato Pie", "Thick", 15)
# print(pie_three.name)

# pie_three.addTopping("Marshmellows").addTopping("Brown Sugar").addSide("Bacon")

# print(pie_three.topping)
# print(pie_three.side)

# print(pie_two.size)
# print(pie_two.topping)