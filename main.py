a= 10
b=10

sum = a + b
sub = a - b
mul = a * b
div = a / b

print("Sum:", sum)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)


# Comments
# This is a single-line comment
"""This is a multi-line comment
that spans multiple lines."""


# variables
# Python is dynamically typed, so you don't need to declare variable types, x = 5

# Data types
# int= 12, float=3.14, str="Hello", bool=True, list=[1, 2, 3], tuple=(1, 2, 3), dict={"a": 1}, set={1, 2, 3}

complex_num = 2 + 3j
print("Complex number:", complex_num)

# Sequence Types (data types that can hold multiple values)

'''
my_list = [1, 2, 3, 4, 5] #List is mutable (can be changed after creation)
my_list.append(6) #Adding an element to the list
my_list[0] = 0 #Changing the first element of the list
print("List:", my_list) 
'''

my_tuple = (1, 2, 3, 4, 5) #Tuple is immutable (cannot be changed after creation)
my_tuple = my_tuple + (6,) #Creating a new tuple by adding an element (since tuples are immutable)
print("Tuple:", my_tuple)
my_tuple = my_tuple[:1] + (0,) + my_tuple[2:] #Changing the first element of the tuple by creating a new one
print("Tuple:", my_tuple)

my_dict = {"name": "Alice", "age": 30} #Dictionary is a collection of key-value pairs
print("Dictionary:", my_dict)

my_set = {1, 2, 3, 4, 5} #Set is an unordered collection of unique elements
print("Set:", my_set)   

# Range data type

my_range = range(0, 10, 2) #Range represents a sequence of numbers, here from 0 to 9 with a step of 2
print("Range:", list(my_range)) #Converting range to a list for display
my_range = range(5) #Range from 0 to 4
print("Range:", list(my_range))
my_range = range(1, 10) #Range from 1 to 9
print("Range:", *my_range) #Unpacking the range to display individual numbers



