names = ["John", "Oscar", "Jacob"]

file = open("names.txt", "w+")
for name in names:
    file.write(name + "\n")
file.close()

file = open("names.txt", "r")
print(file.read())
file.close()
