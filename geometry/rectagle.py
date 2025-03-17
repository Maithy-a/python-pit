# Area = length × width
# Circumference = 2 × (length + width)
# Handles Exceptions and floats

def rectangle():
    while True:
        try:
            length = float(input("Enter Length:"))
            width = float(input("Enter width:"))
            if length < 0 or width < 0:
                raise ValueError("Negative input not allowed")
            area = length * width
            print(f"area:{area:.2f}")
            circumference = 2 * (length + width)
            print(f"circumference:{circumference:.2f}\n")
        except ValueError as e: 
            print(f"Error{e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
rectangle()