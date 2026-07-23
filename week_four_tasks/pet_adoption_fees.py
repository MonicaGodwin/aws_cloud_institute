# Initialize the dictionaries
size_to_fee = {
    "small": 125,
    "medium": 150,
    "large": 175,
    "extra large": 200
}


shelter_pets = {
    "Buddy": "large",
    "Luna": "small",
    "Charlie": "medium",
    "Daisy": "extra large",
    "Stella": "unknown"
}

# Look up Buddy's size and fee using bracket notation
buddy_pet = shelter_pets["Buddy"]
fees = size_to_fee["large"]
print(f"Buddy's addoption fee: ${fees}")

# Check if Luna exists and print her fee
if "Luna" in shelter_pets:
    print(f"Luna's adoption fee: {size_to_fee["small"]}")

# Look up Daisy's fee with default values
daisy_size = shelter_pets.get("Daisy", "100") 
daisy_fee = size_to_fee.get("extra large", "Unknown")
print(f"Daisy's adoption fee: {daisy_fee}")