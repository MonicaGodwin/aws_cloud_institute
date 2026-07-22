user_input = int(input("Enter a number to get the numbers multiple: "))

for number in range(1, 12+1):

    answer = user_input * number
    
    print(f"{user_input} X {number} = {answer}")
    