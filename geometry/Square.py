'''
Create a program that:
1. Prompts the user to enter a number
2. After receiving the input, calculates and displays:
   - The square of the number
   - The square root of the number
   - The cube of the number
   - The cube root of the number

The program should perform all these calculations and show the results for the number entered by the user.

'''

def calc():
    import math
    while True:
        try:
            value = float(input("Enter a value: "))
            if value < 0:
                print("Enter a positive values")
            else:
                square = value ** 2
                sroot = math.sqrt(value)
                cube_root = math.cbrt(value)
                cube = value ** 3
                print(f"square = {square}\n"
                    f"square root = {sroot:.2f} \n"
                    f"cube = {cube} \n"
                    f"Cube root = {cube_root:.2f} \n")
        except ValueError as e:
            print(f" Error {e}")
calc()