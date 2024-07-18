# # This is for Varibales in python

# # Declaring variable
# ## This is a string data type
# MyName = "Toothpick"
# ## This is an integer data type
# Age = 2
# ## This for float data type
# Age = 2.5
# ## This is a boolean data type
# IsTrue = True
# ## List Data type
# List = [1, 2, 3, 4, 5]
# ## Tuples data type
# Tuple = (1, 2, 3, 4, 5)
# ## Set data type
# Set = {1, 2, 3, 4, 5}
# ## Dictionary data type
# Dictionary = {"Name": "Toothpick", "Age": 2, "IsTrue": True}

# ## Complex data type
# Complex = 1 + 2j

# name = "Abhishek"
# age = 13
# worth = 12.5
# game = True
# list_data = [1, 2, 3, 4, 5]
# tuple_data = (1, 2, 3, 4, 5)
# set_data = {1, 2, 3, 4, 5}
# dict_data = {"Name": "Abhishek", "Age": 13, "Worth": 12.5}
# data_complex = 13 + 12.5j
# print (type(name), type(age)) 
# print (type(worth), type(game))
# print (type(list_data), type(tuple_data))
# print (type(set_data), type(dict_data))
# print (type(data_complex))

# name = "Linux"
# print (name[0])
# print (name[1])
# print (name[2])
# print (name[3])
# print (name[4])
# Name = "James"
# say = "Welcome Here! Your age is"
# age = 10
# print (Name, say, age)

# age = 100.5
# my_name = "Captain Dunkurk"
# my_address = "Tijuana, Mexico"
# my_address_num = 2+3j
# print (age, my_name, my_address, my_address_num)

# name = "John"
# message = """
# This is your new class on Python programming
# I hope it get's to your medular oblaganta
# Thank You!
# """
# print (name, message)

# - Tuples are similar to list but they are immutable.
# my_tuple = (1, 2, 3, 4, 5)
# my_tuple[0] = 10
# print (my_tuple)

# list_name = ["Abhishek", "Ankit", "Ankur", "Ankush", "Anupam"]
# list_name[0] = "Toothpick"
# print (list_name)

# ## for Dictionaries
# person = {"Name": "Alice", "Age": 25, "Height": 175}
# car = {'Brand': 'Toyota', 'Model': 'Corolla', 'Year': 2022}
# print (person, car)

#Sets
# numbers = {1, 2, 3, 4, 5}
# print (numbers)

## Data Conversion
# name = str("12")
# print (name)

## Calculate the length of data in a string
# name = (1, 2, 3, 4, 5)
# print (len(name))

# Age, Name = (12, 13, 14, 15, 16), ("Bisi", "Mariam", "Moses", "Ankush", "Anupam")
# print (Age, Name)
# x = "py "
# y = "is "
# z = "Awesome"
# print (x + y + z)

## Operators in python

# x = 2
# y = 5

# ## Carrying out an addition operation
# print (x + y)

## Carrying out an substraction operation
# print (x - y)

# This is the multiplication operation
# print (x * y)

# This is the division operation
# print (x / y)

# This is to carry out modulus operation
# print (x % y)

# This is the exponent operation
# print (x ** y)

# disk_space = 90  # Assume this is the percentage of used disk space

# if disk_space > 80:
#     print("Warning: Disk space is critically low!")
# elif disk_space > 32:
#     print("Caution: Disk space is getting low.")
# else:
#     print("Disk space is sufficient.")

# server_load = 1000  # Assume this is the server load in percentage

# if server_load > 90:
#     print("Critical: Server load is extremely high!")
# elif server_load > 70:
#     print("Warning: Server load is high.")
# elif server_load > 50:
#     print("Caution: Server load is moderate.")
# else:
#     print("Server load is within acceptable limits.")

# x = 10
# y = 20

# if x > 5:
#     if y > 15:
#         print("x is greater than 5 and y is greater than 15")
#     else:
#         print("x is greater than 5 but y is not greater than 15")
# else:
#     print("x is not greater than 5")

## Loops
# For loop

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in numbers:
#     print(num)

#While Loop
# count = 0

# while count < 5:
#     print(count)
#     count += 1
# num = 1
# while num <= 5:
#     break
# print (num + 100)

# num = 1
# while num <= 10:
#     print(num)
#     num += 1
# for num in range(10):
#     if num == 5:
#         break
#     print(num)

# for num in range(10):
#     if num % 2 == 0:
#         continue
#     print(num)

# for i in range(3):
#     for j in range(2):
#         print(i)
        
#         print(j)

# def greet(Toothpick):
#     print("Hello " + Toothpick + " Kikelomo" " Helen")
# greet("Toothpick")

# def my_function():
#     """
#     # Prints a greeting message to the user
#     Hello Loveth Trouble maker

#     ## This function does not take any parameters.

#     ## It print a multiple lines of text or string that includes a greeting message ----> GOTO
#     and a thank you message.
#     I hope this class penetrates your mind
#     Thank you!

#     This function does not return any value
#     """
#     print("Hello Loveth Trouble maker")
#     print("I hope this class penetrates your mind")
#     print("Thank you!")

# my_function()

# Get the username from input
# Prompt the user to enter their name
name = input("Enter your name: ")

# Greet the user with their name
print("Hello, " + name + "!")

# Open 'Store.txt' in append mode, write the name to it, and automatically close the file
with open("Store.txt", "a+") as f:
    f.write(name + "\n")

# Open 'Store.txt' in read mode, read its content, and automatically close the file
with open("Store.txt", "r") as f:
    content = f.read()

# Print the existing content of 'Store.txt'
print("Existing content:\n" + content)



