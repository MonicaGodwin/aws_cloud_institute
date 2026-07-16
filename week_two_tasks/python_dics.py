# Step 1: Create a dictionary with adoption details
pet = {
    "name": "Charlie",
    "age": 1,
    "type": "rabbit",
    "adopted_by": "Sarah",
}

pet["adoption_fee"] = 30

pet["age"] = 2

print(f"your pet name is {pet["name"]}, of age {pet["age"]} adopted by {pet['adopted_by']}. \
{pet["name"]} is of type {pet["type"]} whose adoption fee is {pet["adoption_fee"]}")

if pet["adoption_fee"] > 40:

    print(f"Thank you for adopting {pet['name']}")

else:

    print(f"Thank you {pet["adopted_by"]} for giving {pet["name"]} a wonderfull home.")

