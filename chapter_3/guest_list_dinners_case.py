# 3-4 Guest list
guestlist = ['Kev', 'Elaine', 'Jefry', 'Ommy']

print(f"{guestlist[0]} you're invited to dinner")
print(f"{guestlist[1]} you're invited to dinner")
print(f"{guestlist[2]} you're invited to dinner")
print(f"{guestlist[3]} you're invited to dinner")

# 3-5 Changing Guest List
print(f"Unfournatly {guestlist[3]} can't make it")

guestlist[3] = 'Wilbert'

print(f"{guestlist[3]} is coming instead")

print(f"{guestlist[0]}, {guestlist[1]}, {guestlist[2]} you all still invited")

# 3-6 More Guest
guestlist.insert(0, 'Kevon');
guestlist.insert(2, 'Jose');
guestlist.append('Jay');
print(guestlist)

# 3-7 Shrinking the list.
print("Sorry guys, I can only invite 2 people for dinner")
guestlist.remove('Kevon')
guestlist.remove('Jose')
guestlist.remove('Jefry')
guestlist.remove('Wilbert')
guestlist.remove('Jay')
print(guestlist)
print(f"{guestlist[0]}, {guestlist[1]} only you guys invited")
del guestlist[0]
print(guestlist)
del guestlist[0]
print(guestlist)
print(len(guestlist))