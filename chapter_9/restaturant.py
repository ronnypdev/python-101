class Restaurant:
  """Create a restaurant."""
  def __init__(self, restaurant_name, cuisine_type):
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type

  def describe_restaurant(self):
    print(f"The {self.restaurant_name.title()} is a {self.cuisine_type.title()} cuisine type of restaurant")

  def open_restaurant(self):
    print(f"{self.restaurant_name.title()} is open from Monday to Sunday")


restaurant1 = Restaurant("Freaking Rican", "Puerto Rican type food")
restaurant1.describe_restaurant()
restaurant1.open_restaurant()