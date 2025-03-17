
# Create a program that:
# - Asks the user to input the distance in kilometers and the time in minutes,
# - Then computes the speed using the formula S = D / T.

def speed():
    while True:
        try:
            distance = float(input("Enter the Distance Travelled (km):"))
            time =float(input("Enter the time elapsed(minutes):"))

            if distance < 0:
                print("Distance can't be negative")
            elif time <= 0:
                print("Time must be greater tha zero")
            else:
                meters = distance * 1000
                seconds = time * 60
                hour = time / 60
                speed_mps = meters / seconds
                speed_km_hr = distance / hour

                print(f"Speed was = {speed_mps:.2f} mp/s ")
                print(f"Speed was = {speed_km_hr:.2f} km/hr\n")
        except ValueError:
            print("error")
speed()