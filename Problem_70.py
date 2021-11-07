'''
You are given a function.
int CheckPassword(char str[], int n);
The function accepts string str of size n as an argument. Implement the function which returns 1 if
given string str is valid password else 0.

str is a valid password if it satisfies the below conditions.

– At least 4 characters
– At least one numeric digit
– At Least one Capital Letter
– Must not have space or slash (/)
– Starting character must not be a number
Assumption:
Input string will not be empty.

Example:

Input:
aA1_67
Output:
1

Sample Input:
a987 abC012
Output:
0
'''

def password(input1):
    
    if (len(input1)) < 4:
        return 0
    if input1[0].isdigit():
        return 0
    cup = 0
    dig = 0
    for i in range(len(input1)):
        if input1[i] == " " or input1[i] == "/":
            return 0
        if input1[i]>="A" and input1[i] <= "Z":
            cup = cup +1
        elif input1[i].isdigit():
            dig = dig +1
    if cup >0 and dig > 0:
        return 1
    else:
        return 0




input1 = input("Enter your password : ")
print(password(input1))