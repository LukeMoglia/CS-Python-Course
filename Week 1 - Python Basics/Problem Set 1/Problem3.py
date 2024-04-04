"""
Problem 3

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print:

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print:

Longest substring in alphabetical order is: abc

"""

s = "azcbobobegghaklbeggz"
currentResult = ""
finalResult = ""

# iterate over every character in the string
for char in range(len(s)):
    # if the character is greater than or equal to the previous character, add it to the current result
    if ord(s[char]) >= ord(s[char - 1]):
        currentResult += s[char]
        # if the current result is longer than the final result, update the final result
        if len(currentResult) > len(finalResult):
            finalResult = currentResult
    # if the character is less than the previous character, reset the current result
    elif ord(s[char]) < ord(s[char - 1]):
        currentResult = s[char]
print(finalResult)




