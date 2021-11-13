'''
Statement: Some prime numbers can be expressed as Sum of other consecutive
prime numbers. For example

5=2+3
17=2+3+5+7
41=2+3+5+7 + 11 + 13

Your task is to find out how many prime numbers which satisfy this property are present in the range 3
to N subject to a constraint that summation should always start with number 2.

Write code to find out number of prime numbers that satisfy the above mentioned property in a given range.

Input Format: First line contains a number N
Output Format: Print the total number of all such prime numbers which are less than or equal to N.

Input : 20 
Output: 2

Input : 1000 
Output: 5
'''
input1 = int(input("Enter the range to end :  "))
list1 = [2]
for i in range(3,input1):
    if i == 2 or i == 3 or i == 5:
        list1.append(i)
    elif i%2 != 0 and i%3 != 0 and i%5 != 0:
            list1.append(i)
sum = 0
count = 0
for i in range(len(list1)):
    sum = sum + list1[i]
    if sum <= input1:
        if sum == 5:
            count = count+1
        elif sum%2 != 0 and sum%3 != 0 and sum%5 != 0 and sum%11 != 0 and sum%7 != 0 and sum%13 != 0:
                count = count+1
                print(sum)
print(count)

            
