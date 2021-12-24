
# # F-string
# first_name = "Zen"
# last_name = "Coder"
# age = 27
# print(f"My name is {first_name} {last_name} and I am {age} years old.")


# #string.format()
# first_name = "Zen"
# last_name = "Coder"
# age = 27
# print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# # output: My name is Zen Coder and I am 27 years old.
# print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# # output: My name is 27 Zen and I am Coder years old.

# fruits = ['apple', 'banana', 'orange', 'strawberry']
# vegetables = ['lettuce', 'cucumber', 'carrots']
# fruits_and_vegetables = fruits + vegetables
# print(fruits_and_vegetables)
# salad = 3 * vegetables
# print(salad)


# def get_circle_area(r):
#     #Return (circumference, area) of a circle of radius r
#     c = 2 * math.pi * r
#     a = math.pi * r * r
#     return (c, a)

# # Dictionary
# context = {
#     'questions': [
#         { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
#         { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
#         { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
#         { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
#     ]
# }


# # Conditional
# x = 12
# if x > 50:
#     print("bigger than 50")
# else:
#     print("smaller than 50")
#     # because x is not greater than 50, the second print statement is the only one that will execute

#     x = 55
#     if x > 10:
#     	print("bigger than 10")
#     elif x > 50:
#     	print("bigger than 50")
#     else:
#     	print("smaller than 10")
#     # even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'

#     if x < 10:
#     	print("smaller than 10")
#     # nothing happens, because the statement is false




# # For Loops in Dictionaries 

# capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# # another way to iterate through the keys
# for key in capitals.keys():
#     print(key)
# # output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
# #to iterate through the values
# for val in capitals.values():
#     print(val)
# # output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
# #to iterate through both keys and values
# for key, val in capitals.items():
#     print(key, " = ", val)
# # output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc


# for val in "string":
#     if val == "i":
#         break
#     print(val)
# # output: s, t, r

# for val in "string":
#     if val == "i":
#         continue
#     print(val)
# # output: s, t, r, n, g
# # notice, no i in the output, but the loop continued after the i

# ------------------------------------

# # set defaults when declaring the parameters
# def be_cheerful(name='', repeat=2):
# 	print(f"good morning {name}\n" * repeat)
# be_cheerful()     # output: good morning (repeated on 2 lines)
# be_cheerful("tim")    # output: good morning tim (repeated on 2 lines)
# be_cheerful(name="john")     # output: good morning john (repeated on 2 lines)
# be_cheerful(repeat=6)    # output: good morning (repeated on 6 lines)
# be_cheerful(name="michael", repeat=5)    # output: good morning michael (repeated on 5 lines)
# NOTe: argument order doesn't matter if we are explicit when sending in our arguments!
# be_cheerful(repeat=3, name="kb")    # output: good morning kb (repeated on 3 lines)



# =------------------------------------------------------------------
# DEBUGGINGGGGG

# def multiply(num_list,num):
#     print(num_list, num)
#     for x in num_list:
#         print(x)
#         x *= num
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)

# def multiply(num_list,num):
#     print(num_list, num) # output should be [2,4,10,16] 5
#     for x in num_list:
#         print(x)
#         x *= num
#         print(x)
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)
# output:
# >>>[2,4,10,16] 5
# >>>2
# >>>10
# >>>4
# >>>20
# >>>10
# >>>50
# >>>16
# >>>80
# >>>[2, 4, 10, 16]

# def multiply(num_list,num):
#     print(num_list, num) # output should be [2,4,10,16] 5
#     for x in num_list:
#         print(x)
#         x *= num
#         print(num_list)
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)
# output:
# >>>[2,4,10,16] 5
# >>>2
# >>>4
# >>>10
# >>>16
# >>>[2,4,10,16]
# >>>[2,4,10,16]
# >>>[2,4,10,16]
# >>>[2,4,10,16]


def multiply(num_list,num):
    for x in range(len(num_list)):
        num_list[x] *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output:
# >>>[10,20,50,80]

