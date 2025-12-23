try:
    number = int(input("Please enter a number: "))

    if number % 3 == 0 and number % 5 == 0:
        print("The number",number,"is divisible by both 3 and 5.")
    elif number % 3 == 0:
        print("The number",number,"is divisible by 3 only.")
    elif number % 5 == 0:
        print("The number",number,"is divisible by 5 only.")
    else:
        print("The number",number,"is not divisible by 3 or 5.")

except ValueError:
    print("Invalid input! Please enter an integer.")