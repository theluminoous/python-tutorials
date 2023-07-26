from math import pi
import calendar
rad = float(input("Enter the radius of :"))
print("The area of circle is ",(pi * rad**2))
print("The Volume of Sphare is :",(4/3*pi*rad**3))

color_list = ["red", "blue", "black", "grey"]
print(color_list[0], color_list[2])

date = (28, 12, 2009)
print("The date of Exam is : %i/%i/%i/"%date)
print(abs.__doc__)

y= int(input("Enter the year :"))
m= int(input("Enter the month :"))
print(calendar.month(y,m))
