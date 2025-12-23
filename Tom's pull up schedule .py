file = open("User\Desktop\pull_ups.txt", "r")
n = int(input("Enter the number of days: "))

lines = file.readlines()
for i in range(min(n, len(lines))):
    print(lines[i].strip())

file.close()
