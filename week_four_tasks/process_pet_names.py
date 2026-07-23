# Initialize the shelter pets dictionary.
# IDs that start with 'C' represent cats and 
# those that start with 'D' represent dogs.
shelter_pets = {
    'D1': 'Max',
    'D2': 'Lucy',
    'D3': 'Bailey',
    'D4': 'Charlie',
    'C1': 'Missy',
    'C2': 'Felix'
}

# Print all pet names using dictionary values
print("\n--- All Pet Names ---")
for pet in shelter_pets.values():
    print(pet)

# Print all cat names using direct dictionary iteration
print("\n--- Cat Names Only ---")
for pet in shelter_pets:
    if pet.startswith('C'):
        print(shelter_pets[pet])


# Print dog IDs and names using items()
print("\n--- Dog IDs and Names ---")
for pet, id in shelter_pets.items():
    if pet.startswith('D'):
        print(f"{pet} : {id}")

# Print the total number of pets in the shelter
print("\n--- Total pets in shelter ---")
print(len(shelter_pets))
