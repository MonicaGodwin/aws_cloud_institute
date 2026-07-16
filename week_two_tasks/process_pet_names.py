# Use a for loop with range() to print numbers 1 through 3.
for i in range(3):
    print(f"pets number: {i+1}")

# Prompt the user to enter a pet's name.
pet_name = input("Enter pet's name: ")

print("letters in pet name are:")

# Use a for loop to print each letter in the pet's name.
for name in pet_name:
    print(name)

# Use len() to display the total number of letters in the pet's name.
print(f"the lenght of pet's name is {len(pet_name)}")