import sys
import datetime

# age = int(input("Enter your age :" ))
# print("age is :", age)
# if(age >= 18):
#     print("you can drive a car")
# else:
#     print("you cannot drive a car")


print("Python version")
print(sys.version)
print("Version info.")
print(sys.version_info)

set = datetime.datetime.now()
print("Current time and date is :")
print(set.strftime("%Y-%m-%D   %H:%M:%S"))