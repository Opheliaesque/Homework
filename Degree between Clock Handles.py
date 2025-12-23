hour = int(input("Enter hour: "))
minute = int(input("Enter minute: "))

hour = hour % 12
hour_angle = hour * 30 + minute * 0.5
minute_angle = minute * 6

if hour_angle > minute_angle:
    angle = hour_angle - minute_angle
else:
    angle = minute_angle - hour_angle
if angle > 180:
    angle = 360 - angle
print("Angle between hands =", angle)