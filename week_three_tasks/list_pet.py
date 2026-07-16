# Create a list of pet names.
pets_name = ["buddy", "feline", "canine", "sophie", "lucky"]

print(f"Pet list: {pets_name}")

# Loop forward through the list using range() and print the names with an even index in uppercase.
for i in range(0,len(pets_name), 1):
    if i % 2 == 0:

        print(f"pet list {i}: {pets_name[i].upper()}")
    
print("\nPet list in reverse order:")

# Loop backward through the list using range().
for x in range(len(pets_name)-1, -1, -1,):
    print(f"{x}: pets names: {pets_name[x-1]}")
#   To do 3: Add a loop to print pets in backward order.