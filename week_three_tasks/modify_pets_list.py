# Create a list of pet names.
pets = ["Buddy", "Mittens", "Goldie"]

print("Original list:", pets)

# Use insert() to add a pet at index 2.
print("Inserting 'Fluffy' at index 2")
pets.insert(2 ,"Fluffy")
print("After insert:", pets)

# Use append() to add a new pet to the end of the list.
print("Appending 'Olfie' to the end of the list")
pets.append("Olfie")
print("After append:", pets)

# Use pop() to remove the pet at index 1 and print its name.
print("Removing pet at index 1")
pet_removed = pets.pop(1)
print("pet removed: ", pet_removed)
print("After pop:", pets)