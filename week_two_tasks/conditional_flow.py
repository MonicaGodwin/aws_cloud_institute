# Ask the user how many pets they currently own
number_of_pets = input("Enter number of pets owned: ")

# Convert the input to an integer
input_convert = int(number_of_pets)

if input_convert > 5:
    print("Not eligible for adoption")

elif input_convert == 5:
    print("You have 5 pets you should consider adopting some other time") 

elif input_convert == 0:
    print("Ready to adopt your first pet")





# Use conditional statements to determine eligibility for adoption