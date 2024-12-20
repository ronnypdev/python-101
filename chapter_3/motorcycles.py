motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# motorcycles[0] = 'ducati'

# append() adds an item to the end of this list
motorcycles.append('ducati')

# insert() adds an item to any position within the array
motorcycles.insert(0, 'ktm')
print(motorcycles)

# if you know the position(the index) of an item in the list use del to
# remove that particular item's position
del motorcycles[0]
print(motorcycles)

# the pop() method removes the last item in a list,
# but it lets you work with that item after removing it.
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)

# the remove() method removes the item from a list base on
# its value not the position
motorcycles.remove('suzuki')
print(motorcycles)
