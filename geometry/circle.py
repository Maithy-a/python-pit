def circle ():   
    while True:
        pi = 3.14
        try:
            radius = float(input("Please enter the radius of the circle:"))
            if radius < 0 :
                 raise ValueError("Negative values not accepted.")
             
             # Circumference: C = 2 * pi * r
            circumfrence = 2 * pi * radius
            print(f"Circumfrence: {circumfrence}")
            
            # Area: A = pi * r^2
            Area = 2 * pow(radius,2)
            print(f"Area: {Area}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
circle()