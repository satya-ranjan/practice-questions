'''
Given an integer 'n' (1 <= n <= 10 ⁹), find the number of positive integers which are less than or equal
to n and also are relatively prime to n. An integer a is relatively prime to another integer bif gcd(a,b)=1

You need to fill in a function that takes integer 'n' as an input and returns the number of positive
integers which are less than or equal to n (positive integers <= n) and that are relatively prime to n

Input Specification:
    input1: An integer in the range of 1 <=inputt <= 10 °

Output Specification:
    Return the number of positive integers which are less than or equa to in and that are relatively prime
    to n

Example 1:
input : 6
output : 2

Explanation : 1 and 5 are relatively prime to 6 hence the count returned is 2
'''
def prime(num):
    flag = False
    count = 0
    if num > 1:
        for i in range(2,num):
            if (num%i==0):
                flag = True
            else:
                flag = False
                print(num)
    if flag:
        count = count+1
    print(count)
prime(4)
