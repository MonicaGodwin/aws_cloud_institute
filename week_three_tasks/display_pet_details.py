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
    print(
        f"pet name: {pet["name"]}",
        f"pet type:{pet["type"]}",
        f"pet age: {pet["age"]}"
    )

    if pet["age"] <= 2:
        print(f"{pet["name"]} is very young")
