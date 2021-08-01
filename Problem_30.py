'''
input : An integer which you have to calculate factorial

output : Return an integer representing the number of traling Zeroes.

Example 1:

input : 5
output : 1

Example 2:

input : 4
output: 0
Exalation:
The factorial of 4 is 24. The number of traling zeroes = 0 
'''

def factorial(input_num):
    mult_num = 1
    count = 0
    for i in range(1,input_num+1):
        mult_num = mult_num*i
    digit = [int(i) for i in str(mult_num)]
    for i in digit:
        if i == 0:
            count = count+1
    print(count)


input_num = int(input("Enter the number : "))
factorial(input_num)