number = input("Enter a number, that is multiples of 10: ")
number = int(number)

if number % 10 == 0:
  print(f"\nThe number {number} is multiple of 10.")
else:
  print(f"\nThe number {number} is not a multiple of 10.")