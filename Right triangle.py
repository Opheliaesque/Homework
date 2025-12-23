a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

if a*a + b*b == c*c:
    print("Right triangle")
else:
    print("Not a right triangle")
