#1
#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

# a = []
# for i in range (2000,3201):
#     if (i % 7 == 0) and (i % 5 != 0):
#        a.append(str(i))
# print(','.join(a))


#2
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x - 1)
# x = int(input())
# print(fact(x))

#3
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such
# that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# a = dict()
# x = int(input())
# for i in range(1, x+1):
#     a[i] = i*i
# print(a)

















