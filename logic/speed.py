'''
 Formula
  S = D / T
  make a program that
  Prompt the user to enter the value of the distance in kilometers
   and Time in minutes;
  then calculates the speed
'''

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
                speed_kmhr = distance / hour

                print(f"Speed was = {speed_mps:.2f} mp/s ")
                print(f"Speed was = {speed_kmhr:.2f} km/hr\n")
        except ValueError:
            print("error")
speed()