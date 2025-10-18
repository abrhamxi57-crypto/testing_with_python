# Asking for user details

name = input("Enter your name: ")
favorite_food = input("Enter your favorite food: ")
current_year = int(input("Enter the current year: "))
age = int(input("Enter your age: "))

# Calculating birth year

birth_year = current_year - age

# Display personalized greeting and birth year
print(f"\nHello, {name}! You love {favorite_food}.")
print(f"You were born in {birth_year}.")
