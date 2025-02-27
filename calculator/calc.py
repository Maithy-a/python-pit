def calculator():
    print("\nSimple calculator")
    while True:
        print("Please select an operation:",
              "\n1. Addition",
              "\n2. Subtraction",
              "\n3. Multiplication",
              "\n4. Division",
              "\n5. Quit")
        operation = input("Enter value: 1,2,3,4,or 5: ").strip()
        
        if operation == "5":
            print("Thank you for using the calculator... Exiting!!\n")
            break
            
        try:
            first_num = float(input("Enter your first number: ").strip())
            second_num = float(input("Enter your second number: ").strip())            
        
            if operation == "1":
                ans = first_num + second_num
                print(f"Result: {ans}")
            elif operation == "2":
                ans = first_num - second_num
                print(f"Result: {ans}")
            elif operation == "3":
                ans = first_num * second_num
                print(f"Result: {ans}")
            elif operation == "4":
                if second_num == 0:
                    print("Division by zero is not allowed")
                else:
                    ans = first_num / second_num
                    print(f"Result: {ans:.2f}")
            else:
                print("Invalid input, please enter a valid number")
                
        except ValueError:
            print("Invalid input, please input valid numbers")

calculator()