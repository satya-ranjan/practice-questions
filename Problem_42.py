
'''
Armstrong Number

An Ambones a number such hur the set of the the powes of d 371 is an Ambrong number of 3 digits since
3³+7³+1³ = 371 Write a Runction to check whether a number is an Armstrong number or not For example
So nowset, when as the number of digits in the

Input Specification: input1: An integer value

Output Specification:

Output: String indicating of the"Yes", others ber an Amersan Armstrong r not. If the g return "No"


Example 1

input: 471

Output: Yes

Explanation:

The sum of the individual cubes of each dpt of the number is equus to the number itself as 145-153 Hence, Yes returned

Example 2

input1: 125

Output: No

Explanation:

The sum of the individual cubes of each digit of the number is not equal to the number itself as 14245 134 Hence. No is returned
'''

input1 = input("Enter the in put you watnt to take : ")
len1 = len(input1)
num = 0
for i in range (len(input1)):
    num = num + (int(input1[i]) ** len1)
if num == int(input1):
    print("YES")
else:
    print("NO")


