# sort() method sorts the list ascending(alphabetical order) by default
# or it will sort the list depending on the criteria you specify
# this method also changes the original order of the list
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# reverse alphabetical order
cars.sort(reverse=True)
print(cars)

# sorted() lets you display your list in a particular order
# but doesn't affect the original order of the list.
print("\nHere is the sorted list:")
print(sorted(cars))

# reverse() it reverses the original order of the list
# doesn't sort backward alphabetically, it simply reverses the order of the list
# changes the order of the list permanently but you can revert to the original
# order anytime by applying reverse() to the same list a second time
cars.reverse()
print(cars)

# len() finds the length of the list
print(len(cars))