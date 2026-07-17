# Create a list of dictionaries representing pets.
pets = [
    {
        "name": "Buddy", 
        "type": "Dog", 
        "age": 3
    },
    {
        "name": "Mittens", 
        "type": "Cat", 
        "age": 5
    },
    {
        "name": "Goldie", 
        "type": "Fish", 
        "age": 2
    },
]

# Use a direct iteration for loop to iterate over the list of dictionaries.
for pet in pets:
    # pet["adoption_priority"] = "High"

    if pet["age"] > 2:
        pet["adoption_priority"] = "High"

    else:
        pet["adoption_priority"] = "Normal"

print(pets)






