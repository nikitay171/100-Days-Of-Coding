#7
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
#
# Hints:
# Note: In case of input data being supplied to the question, it should be assumed
# to be a console input in a comma-separated form.

# inp_str = input()
# dimension = [int(x) for x in inp_str.split(',')]
# row = dimension[0]
# col = dimension[1]
#
# multi_list = [[0 for c in range(col)] for r in range(row)]
# for i in range(row):
#     for j in range(col):
#         multi_list[i][j] = i*j
# print(multi_list)

# 8
# Question:
# Write a program that accepts a comma separated sequence of words as input and prints the words
# in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

# In case of input data being supplied to the question, it should be assumed to be a console input.
# item is list we add them as list and sort. join add data with , as separator

# items=[x for x in input().split(',')]
# items.sort()
# print(','.join(items))

# 9
# Question£º
# Write a program that accepts sequence of lines as input and prints the lines after making
# all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


# lines = []
# while True:
#     s = input()
#     if s:
#         lines.append(s.upper())
#     else:
#         break;
# for sentence in lines:
#     print(sentence)

# 10
# Write a program that accepts a sequence of whitespace separated words as input and prints the words
# after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

# inp_str = input()
# a = [x for x in inp_str.split(" ")]
# b = sorted(list(set(a)))
# print(" ".join(b))



