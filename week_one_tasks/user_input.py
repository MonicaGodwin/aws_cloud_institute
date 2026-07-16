# Prompt the user for pet details.
pet_name = input("Enter your pet's name: ")
pet_type = input("Enter your pet's type: ")
pet_age = input("Enter your pet's age: ")

# Format the pet description using an f-string.
pet_description = f"Your pet's name is {pet_name},the pet type is {pet_type} and the pet is {pet_age} years old"

# Convert the description to uppercase.
uppercase_description = pet_description.upper()

# Ask how many treats the pet gets per day.
treats_per_day = int(input("Enter the amount of treats per day "))
treats_per_week = treats_per_day * 7

# Replace the pet type.
updated_description = pet_description.replace("dog", "canine")
updated_description = pet_description.replace("cat", "feline")

# Display a thank you message.
thank_you_message = "Thank you for patronizing AnyPet Company.\n We'll like to see you again"  # Add escape characters here.

# Print all results.
print("\nPet Profile:")
print(pet_description)
print("Uppercase Description:", uppercase_description)
print("Treats per week:", treats_per_week)
print("Updated Description:", updated_description)
print(thank_you_message)