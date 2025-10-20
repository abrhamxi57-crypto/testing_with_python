
name = input("Enter your name: ")
favorite_food = input("Enter your favorite food: ")
current_year = int(input("Enter the current year: "))
age = int(input("Enter your age: "))

# Calculate birth year
birth_year = current_year - age

# Print a personalized greeting
print("Hello",name , "It's great to meet you.")
print("You love",favorite_food )
print("You were born in ",birth_year)
