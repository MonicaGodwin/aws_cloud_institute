while True:
    sel_operation = input("enter an operation or done to end the operation: +, -, *, /, %, **: ")

    if sel_operation.lower() == "done":
            print("Thanks for using my mini calculator")
            break

    user_input_1 = int(input("enter a number: "))
    user_input_2 = int(input("enter another number: "))

    if sel_operation == "+":
        print("result: ", user_input_1 + user_input_2)
        
    elif sel_operation == "-":
        print("result: ", user_input_1 - user_input_2)
        
    elif sel_operation == "/":
        print("result: ", user_input_1 / user_input_2)
        if user_input_2 == 0:
            print("can't divide a number by zero!")
       
    elif sel_operation == "%":
        print("result: ", float(user_input_1) % float(user_input_2))
        
    elif sel_operation == "*":
        print("result: ", user_input_1 * user_input_2)

    elif sel_operation == "**":
        print("result: ", user_input_1 ** user_input_2)

    else:
        print("invalid operation")

    




 