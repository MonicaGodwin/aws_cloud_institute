# Create a list of update names that represents the update inventory.
pets = ["Buddy", "Goldie", "Spike"]

# Print the original list of pets.
print("Original list of pets:", pets)

# Define a list of updates whose elements are dictionaries of actions.
updates = [
    {
        "action": "add", 
        "name": "Mittens"
    },
    {
        "action": "adopt", 
        "name": "Goldie"
    },
    {
        "action": "promote", 
        "name": "Bella"
    },
]

for update in updates:
    if update["action"] == "add":
        if update["name"] not in pets:

            pets.append("mitten")
            print("mitten was added")

    elif update["action"] == "adopt":
        if update["name"] in pets:
            pet_removed = pets.pop(1)
            print("Pet adopted: ", pet_removed)

    elif update["action"] == "promote":
        if update["name"] not in pets:
            pets.insert(0, "Bella")
            print("Pet Bella was promoted")

print("Final list of pets:", pets)


