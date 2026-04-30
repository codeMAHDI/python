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

# maya++ language name


# Data types checking
print("Type of a:", type(a))
print("Type of b:", type(b))
print("Type of sum:", type(sum))
print("Type of sub:", type(sub))
print("Type of mul:", type(mul))
print("Type of div:", type(div))
print("Type of complex_num:", type(complex_num))
print("Type of my_tuple:", type(my_tuple))
print("Type of my_dict:", type(my_dict))
print("Type of my_set:", type(my_set))
print("Type of my_range:", type(my_range))
print("Type of my_range (as list):", type(list(my_range)))


# Immutable vs Mutable data types
# Immutable data types: int, float, str, tuple, frozenset
# Mutable data types: list, dict, set

# Example of immutability
x = 10
print("Original x:", x)
first_id = id(x) # Get the memory address of the original integer object
print("Memory address of original x:", first_id)
x = 20 # This creates a new integer object and assigns it to x, the original integer (10) remains unchanged
second_id = id(x) # Get the memory address of the new integer object
print("Memory address of updated x:", second_id)
print("Updated x:", x)

# Example of mutability
my_list = [1, 2, 3]
print("Original list:", my_list)
my_list.append(4) # This modifies the original list object
print("Updated list:", my_list)

list1 = [1, 2, 3]
first_id= id(list1) # Get the memory address of the original list object
print("Memory address of original list:", first_id)
list1[0]= 12
second_id= id(list1) # Get the memory address of the modified list object
print("Memory address of modified list:", second_id)

# Type conversion
# Example of type conversion. Explicit and implicit type conversion
# Explicit type conversion (casting)=> int(), float(), str(), list(), tuple(), dict(), set() 
# Implicit type conversion (coercion)=> happens automatically when performing operations between different data types, e.g., 5 + 3.14 results in 8.14 (int is converted to float)
# Explicit type conversion
x=10
y=float(x) # Converting integer to float
print("Explicit type conversion (casting):", y)

#Implicit type conversion
a= 5
b= 3.14
c= a+b # int is automatically converted to float
print("Implicit type conversion (coercion):", c)


