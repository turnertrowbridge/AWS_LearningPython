# Strings
# first_name = "Monty"
# last_name = "Python"
# print("Your name is {} {}".format(first_name, last_name))
#
# print(f"Your name is {first_name} {last_name}")

# Number types
# my_int = 50
# my_double = 50.000
# my_float = 50.0
# sentence = "Your total is "

# print(sentence + str(my_double) + f" or {my_float} or {my_int}")

# # Dictionary
# user = {"first_name": "Michael"}
# print(user)
# print(user["first_name"])
#
# # Add new value
# user["family_name"] = "Byron"
# print(user)
#
# # Modify Value
# user["family_name"] = "Lovelace"
# print(user)
#
# # Delete key-value pair
# del user["family_name"]
# print(user)
#
# # Empty Dictionaries
# account_details = {}
# account_details1 = dict()

# Lists
fruit = ["apples", "oranges", "bananas"]
fruits = []
fruits2 = list()
print(fruit[1])
len(fruit)
print(fruit[-1])

fruit.append("pears")
print(fruit)

fruit.insert(3, "kiwi")
print(fruit)

print(sorted(fruit))

fruit.sort()
print(fruit)

fruit.reverse()
print(fruit)

del fruit[1]
print(fruit)

fruit.remove("apples")
print(fruit)

last_fruit = fruit.pop()
print(last_fruit)

print(type(last_fruit))