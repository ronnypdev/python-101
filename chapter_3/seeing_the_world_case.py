# 3-8 Seeing the World
locations = ["paris", "us", "naples", "new zealand", "australia", "japanese"]
print(locations)

# print sorted() list
print(sorted(locations))
# list still original order
print(locations)

sorted_reverse_location = sorted(locations, reverse=True)
print(sorted_reverse_location)
# list still original order
print(locations)

# Using reverse method
locations.reverse()
print(locations)

# Using reverse method a second time
locations.reverse()
print(locations)

# Using the sort() method
locations.sort()
print(locations)

# Using the sort() method with reverse argument
locations.sort(reverse=True)
print(locations)
