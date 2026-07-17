import json

# Create a dictionary representing a pet.
pets = {
    "name": "Mittens",
    "age": 2,
    "type": "cat",
}
pets["color"] = "Brown"

dict_to_json = json.dumps(pets)

print(dict_to_json)

json_to_dict = json.loads(dict_to_json)

print(f"{json_to_dict["name"]} is a {json_to_dict["type"]} with a {json_to_dict["color"]} color fur.")
