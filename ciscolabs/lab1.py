def value():
    while True:
        try:
            x = float(input("Enter the value of x: "))
            y = 1/(x + 1/(x + 1/(x +1/(x))))

            print (f"The value of y is: {y}\n ",)
        except ValueError:
            print("Enter a numerical value.\n")
value()
