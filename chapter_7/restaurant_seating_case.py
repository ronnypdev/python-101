customers = input("How many people are in the group? : ")
customers = int(customers)

if customers >= 8:
  print(f"You'll have to wait for a table")
else:
  print(f"Your table is ready")