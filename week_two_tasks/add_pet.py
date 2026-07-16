store_accepting_pet = True

pet_added = 0

# Use a while loop to add new pets to the store
while store_accepting_pet:

    pet_type = input("Input a pet type (or 'done' to finish): ")

    if pet_type == "done":

        store_accepting_pet = False
    else:
        pet_added += 1
        
    print(f"Added {pet_added} to the inventory\n")   

print(f" the number of pets added is: {pet_added}")
