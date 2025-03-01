# Area: A = pi * r^2
# Circumference: C = 2 * pi * r
# Handle floats and Exceptions(errors)

def circle ():   
    while True:
        pi = 3.14
        try:
            radius = float(input("Please enter the radius of the circle:"))
            if radius < 0 :
                 raise ValueError("Negative values not accepted.")
            circumference = 2 * pi * radius
            print(f"circumference: {circumference:.2f}")
            area = 2 * pow(radius,2)
            print(f"Area: {area:.2f}\n")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
circle()