# Create a list of pet names.
pets = ["buddy", "feline", "canine", "sophie", "lucky"]

print("Original Pet List:", pets)   # Print the original pet list.

# Use a counting loop to modify the pet names and indicate they are on sale.
for pet in range(len(pets)):
    # print(f"{pet+1}: pet {pets[pet]} -ON SALE ")
    pets[pet] = pets[pet] + " - ON SALE!"

print("Updated Pet List:", pets)   