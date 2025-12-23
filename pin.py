pin = input("Set a pin: ")
try:
    int(pin)
    print("Pin code created")
except ValueError:
    print("Please enter a number")
