Coffee = ["Latte", "Americano","Espresso","Cappuccino","Macchiato"]

choice = int(input("Enter the coffee of your choice: "))

try:
    if choice <= len(Coffee):
        print("Enjoy your",Coffee[choice])
    else:
        print("Your coffee choice is invalid.")

finally: print("Have a good day!",)