import sys

def calculate_speed(distance, time):
    return distance / time

if _name_ == "_main_":

    if len(sys.argv) == 3:
        distance = float(sys.argv[1])
        time = float(sys.argv[2])
    else:
        distance = float(input("Enter distance (km): "))
        time = float(input("Enter time (hours): "))

    if time == 0:
        print("Time cannot be zero!")
    else:
        speed = calculate_speed(distance, time)
        print(f"Speed = {speed} km/hr")