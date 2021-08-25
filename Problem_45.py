'''
Given an array of integers representing measurements in inches, write a program to calculate the total of measurements in feet. Ignore the measurements those are less than a feet (e.g. 10)

Note:

You are expected to write code in the find TotalFeet function only which will receive the first parameter as the number of items in the array and second parameter as the array itself. You are not required to take input from the console.

Example

Finding the total measurements in feet from a list of 5 numbers

Input

input1: 5 input2: 18 11 27 12 14

Output

6.833333333333333

'''

def FindTotalFeet(input2):
    sum = 0
    feet = 1
    for i in range (len(input2)):
        if input2[i] > 10:
            feet = input2[i]/12
            sum = sum + feet
            
    print(sum)

input1 = int(input("Enter how many input you want to take : "))
input2 = list(map(int, input("Enter the input separeted by space : ").strip().split(" ")))[:input1]

FindTotalFeet(input2)