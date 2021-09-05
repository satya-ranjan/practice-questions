'''
Single File Programming Question

Your little brother has a math assignment to find whether the given number is a power of 2. 
If it is a power of 2 then he has to find the sum of the digits. If it is not a power of 2, 
then he has to find the next number which is a power of 2. He asks for your help to validate his work. 
But you are already busy playing video games. Develop a program so that your brother can validate his 
work by himself.

Example 1

Input

64

Output

Yes

10

Example 2

Input

133

Output

No
'''


def power(input1):
    sum = 0
    if (int(input1) & (int(input1) - 1)) == 0:
        print("yes")
        for i in range(len(str(input1))):
            sum = sum + int(input1[i])
        print(sum)
    else:
        print("No")









input1 = input()
power(input1)