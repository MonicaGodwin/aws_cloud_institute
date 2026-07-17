import random

random_number = random.randint(1, 10)

print("Guess a number between 1 and 10.")

while True:
    user_guess = input("Enter your guess: ")

    user_guess = int(user_guess)

    if user_guess < 1 or user_guess > 10:
        print("guess out of range")

    elif user_guess > 5:
        print("guess too high")

    elif user_guess <= 5:
        print("guess too low")
        
    else:
        print("Congratulations!!! you guessed correctly")
        break
   