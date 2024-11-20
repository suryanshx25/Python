# import sys

# print(sys.version)
# print(sys.version_info)

# import datetime

# now = datetime.datetime.now()

# print(now)

# r = float(input("Enter Radius : "))
# area = 3.14*r*r
# print(area)

# a = input("Enter first name : ")
# b = input("Enter second name : ")

# print(b + " " + a)  # Output: John Jane

values = input("Enter some comma-separated numbers : ")

list = values.split(",")
tuple = tuple(list)
print('List : ', list)
print('Tuple : ', tuple)