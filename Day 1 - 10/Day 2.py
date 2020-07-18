# 4
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which
# contains every number. Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# values = input()
# l = values.split(",")
# t = tuple(l)
# print(l)
# print(t)

# 5
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# class Test(object):
#     def __init__(self):
#        self.s = ""
#
#     def getString(self):
#         self.s = input()
#
#     def printString(self):
#         print(self.s.upper())
#
# Obj = Test()
# Obj.getString()
# Obj.printString()


#6
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24
#
# Hints:
# If the output received is in decimal form, it should be rounded off to its nearest value
# (for example, if the output received is 26.0, it should be printed as 26)
# In case of input data being supplied to the question, it should be assumed to be a console input.

# import math
# c=50
# h=30
# value = []
# items=[x for x in input().split(',')]
# for d in items:
#     value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
# print(','.join(value))






