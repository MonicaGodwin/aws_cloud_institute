# String formatting with f-strings.
pet_name = "Buddy"
pet_price = 49.99
formatted_message = f"The pet {pet_name} costs ${pet_price:.2f}."
print(formatted_message)

# Escape character# Write a string with pet details.
pet_details = "Buddy is a 3-year-old dog "


# Use an f-string to preface pet_description with "Pet description:".
formatted_description = f"pet desciption: {pet_details}"


# Add a string with a newline character and a thank you message.
message = formatted_description + \
    "with deep black eyes,\n And have black spots on his brown fur\n Thanks for coming to AnyPet Company"

# Extract the pet's name from pet_details using slicing.
pet_name =   pet_details[:5]

# Convert the formatted_description to uppercase.
uppercase_description = message.upper()

# Replace "dog" with "canine" in the formatted_description.
updated_description = message.replace("dog", "canine")

# Print the results.
print("Formatted string:", formatted_description)
print("Message with newline:", message)
print("Pet name:", pet_name)
print("Uppercase description:", uppercase_description)
print("Updated description:", updated_description)
store_message = "Welcome to AnyCompany Pet Society!\nWe love pets of all kinds.\tShop with us today!"
print(store_message)