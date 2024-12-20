# A list comprehension allows you to generate multiple lines of code
# in just one line of code. A list comprehension combines the for loop and
# the creation of the elements into one line and automatically appends each new element
squares = [value** 2 for value in range(1, 11)]
print(squares)