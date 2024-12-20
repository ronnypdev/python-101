# range() function that generates a series of numbers
for value in range(1, 6):
  print(value)

# list() converts results from range()
# to a list(Array)
numbers = list(range(1, 6))
print(numbers)

# range() can also be use to skip numbers
even_numbers = list(range(2, 11, 2))
print(even_numbers)