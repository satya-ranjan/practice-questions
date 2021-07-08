'''
Program to reverse the string after removing duplicates

INPUT
-> google
OUTPUT
->elog
'''
string = input("Enter the string : ")
str = ""

for i in string:
    if i not in str:
        str = str + i
rev = str[::-1]
print(rev)