# Area = length × width
# Circumference = 2 × (length + width)
# Handles Exceptions and floats

def rectangle():
    while True:
        try:
            length = float(input("Enter Length:"))
            Width = float(input("Enter Width:"))
            if length < 0 or Width < 0:
                raise ValueError("Negative input not allowed")
            Area = length * Width
            print(f"Area:{Area:.2f}")
            Circumference = 2 * (length + Width)
            print(f"Circumference:{Circumference:.2f}\n")
        except ValueError as e: 
            print(f"Error{e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
rectangle()