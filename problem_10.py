'''
Identify Palindrome


For a given positive number num, identify the palindrome formed by performing the following operations-


Add num and its reverse
Check whether the sum is palindrome or not. If not, add the sum and its reverse and repeat the process until a 
palindrome is obtained


For example:

If original integer is 195, we get 9,339, as the resulting palindrome after the fourth addition:

Input format: Read num from the standard input stream.
Output format: Print the palindrome calculated to the standard output stream.
Example 1

Sample input:

124
Sample output:

545
Explanation:

The sum of 124 and its reverse 421 is 545 which is a palindrome.

Example 2

Sample input:
4
Sample output:
8

Explanation:

The sum of 4 and its reverse 4 is 8 which is a palindrome.



Code Solution in Python:

Input: 124

'''
def check(num):
    N = num[::-1]
    sum = int(num) + int(N)

    if str(sum) == str(sum)[::-1]:
        print(sum)
    else:
        return check(str(sum))
        
num = input(" Enter the number ")
check(num)

