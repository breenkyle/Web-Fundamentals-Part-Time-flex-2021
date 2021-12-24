# # x = 2

# # if x < 3:
# #     print(x)

# # Data Types

# ## Booleans

# # is hungry = True

# ## Numbers

# # int          COMMAND + /
# some_int = 42
# # float
# some_float = 4.2
# # some.float = 3.14
# # Complex
# # complex = 3j   probably never use this

# print(type(42))

# age ="45"
# # string ^
# print(int(age) + 1)
# print(int(age) + str(1))

# python sees 1 as an integer.
#paranthesis "age"
# make 1 a string - put "str" in front

# truck_name = "Rob's Pie Truck"
# review = 3.14
# print(truck_name)
# print(len(truck_name))
# print(f"{truck_name} from Chicago has {review} reviews")
# # F string  - string of text after an F
# # DO IT THIS WAY ^^^^^^^


# emplty_list = []
# ninjas = ['Rozen', 'KB', 'Oliver']
# print(ninjas[2])
# ninjas.append("Michael")
# print(ninjas)
# ninjas.pop()
# print(ninjas)
# ninjas.pop(0)
# print(ninjas)


# list slice
# some_list = [ 3.14, 8.5, 14, 55, 24, 45 ]
# first_three = some_list[:3]
# print(first_three)
# first_three = some_list[2:5]
# print(first_three)
# last_three = some_list[4:]
# print(last_three)

# Tuple - List that cannot change!
# Immutable
# date of birth, or a location (coordinates)



# tuple_data = ('physics', 'history', '1994', '1999')
# # tuple_data.append('Chicago') NOT ALLOWED
# print(tuple_data)


# Dictionary
some_dictionary = {
    # key : value pair
    "location" : "Oak Park",
    "state" : "IL"
}

print(some_dictionary["location"] + some_dictionary["state"])