
#square root finder
import  math
def square ():
    while True:
        try:
            val = float(input("\nEnter a value to find its Square root:"))
            if val < 0:
                print("Cannot find square roots of negative numbers")
            else:
                sroot = math.sqrt(val)
                print(f"The square root of {val} is: {sroot:.2f}")
        except ValueError:
            print("Enter a valid Value")
square()
