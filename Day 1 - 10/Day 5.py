# Question 14
# Level 2
# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9
#
# uc = 0
# lc = 0
# inp_str = input()
# for i in inp_str:
#     if i.isupper():
#         uc += 1
#     elif i.islower():
#         lc += 1
#     else:
#         pass
# print("UPPER CASE", uc)
# print("LOWER CASE ", lc)

# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# 
# tot = 0
# a = input()
# n1 = int("%s" % a)
# n2= int("%s%s" % (a, a))
# n3 = int("%s%s%s" % (a, a, a))
# n4 = int("%s%s%s%s" % (a, a, a, a))
#
# tot = n1 + n2 + n3 + n4
# print(tot)

