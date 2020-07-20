# 11
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input
# and then check whether they are divisible by 5 or not. The numbers that are
# divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# val = []
# data = [x for x in input().split(',')]
# for p in data:
#     res = int(p, 2)
#     if res % 5 == 0:
#         val.append(str(res))
# print(','.join(val))

# 12
# Write a program, which will find all such numbers between 1000 and 3000 (both included)
# such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# val = []
# for i in range(1000, 3001):
#     s = str(i)
#     if int(s[0]) % 2 == 0 and int(s[1])%2 == 0 and int(s[2]) % 2 == 0 and int(s[3]) % 2 == 0:
#         val.append(str(i))
# print(','.join(val))

# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

# s = input()
# d = {"DIGITS": 0, "LETTERS": 0}
# for c in s:
#     if c.isdigit():
#         d["DIGITS"]+=1
#     elif c.isalpha():
#         d["LETTERS"]+=1
#     else:
#         pass
# print("LETTERS", d["LETTERS"])
# print("DIGITS", d["DIGITS"])









