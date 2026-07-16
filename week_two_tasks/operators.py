# Prompt user for input
pet_name = input("Enter pet's name: ")
pet_owner = input("Enter pet's owner's name: ")

# Calculate the lengths of both names
 
pet_name_lenght = len(pet_name)
pet_owner_leght = len(pet_owner)

# Compare the lengths and print results
print(pet_name_lenght > pet_owner_leght)
print(pet_name_lenght == pet_owner_leght)

# Prompt user for the number of pets and maximum capacity

pets_number = input("Enter number of pets: ")
max_capacity = input("Enter pet's maximum capacity: ")

# Convert inputs to integers
converted_pet_number = int(pets_number)
converted_max_capacity = int(max_capacity)


# Compare pets in store to maximum capacity
print(converted_pet_number > converted_max_capacity)  # Add > comparison
print(converted_pet_number < converted_max_capacity)  # Add < comparison