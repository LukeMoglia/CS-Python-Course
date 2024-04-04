"""
Problem 2

Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print:

Number of times bob occurs is: 2

"""

s = "azcbobobegghakl"
count = 0

# iterate over every character in the string
for bob in range(len(s)):
    # if the character is 'bob', increment the count
    if s[bob:bob+3] == "bob":
        count += 1

print("Number of times bob occurs is: " + str(count))