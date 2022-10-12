# -------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mohdk
#
# Created:     11-10-2022
# Copyright:   (c) mohdk 2022
# Licence:     <your licence>
# -------------------------------------------------------------------------------

# basic calculator in python by user input:
first = input("enter First value ? : ")
operation = input("Enter operator for addition: (+), for subtraction: (-), for multiply: (*), for divide: (/), for reminder: (%) : ")
second = input("Enter second value ? : ")
first = float(first)
second = float(second)
if operation == '+':
    sum = first + second
    sum = float(sum)
    print("Addition Result : ", sum)
elif operation == '-':
    sum = first - second
    sum = float(sum)
    print("Subtraction Result : ", sum)
elif operation == '*':
    sum = first * second
    sum = float(sum)
    print("Multiply Result : ", sum)
elif operation == '/':
    sum = first / second
    sum = float(sum)
    print(" Divide Result : ", sum)
elif operation == '%':
    sum = first % second
    sum = float(sum)
    print("Reminder Result : ", sum)
else: print("Unknown operation, please enter only listed operator")