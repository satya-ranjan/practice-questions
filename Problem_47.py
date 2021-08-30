'''
Single File Programming Question

Kali's friend gave him a tough task to test his problem-solving skills. Given a decimal number n, write a program to find its equivalent number to the base 5.

Example

Input

754

Output

11004

Explanation

You have to keep dividing by 5 and continue this for all quotients until '0' and keep track of all remainders

So,

754-5*150+4

150=5 30+0

30=5*6+0

6=5*1+1

1=50+1

Write all the remainders in reverse 11004
'''



num = int(input("Enter the number of input you want to take : " ))
rem = num
divide = []
rev=" "
for i in range(5): 
    if rem/5 != 0 :
        divide.append(int(num % 5))
        num = num / 5 
    rev = (divide)[::-1]
for i in rev:
    print(i, end="")

