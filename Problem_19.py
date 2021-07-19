'''
Write a program to retum the difference between the largest and smallest numbers from an array of positive 
integers

Note:
You are expected to write code in the findLarge SmallDifference function only which will receive the first parameter as the number of items
in the array and second parameter as the array itself. You are not required to take input from the console
Example
Finding the difference between the largest and smallest from a list of 5 numbers Input
input:
5
input2: 10 11 7 12 14
Output
7
'''
def findLargeSmallDifference(take_input,input_are):
    sub = 0
    min_n = 0
    max_m = 0
    for i in range(len(input_are)):
        min_n = min(input_are)
        max_m = max(input_are) 
        sub =  max_m - min_n 
    print(sub) 


take_input=int(input("How many input do you want to take : "))
input_are = list(map(int, input("Enter the number of input u want to take :").strip().split(" ")))[:take_input]
findLargeSmallDifference(take_input,input_are)
