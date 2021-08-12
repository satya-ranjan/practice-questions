'''
Write A Program To Input String And Display Count Of All Permutations Of Strings Without Using Any
Built In Functions

Input

abc

Output

6
'''

str_input = input("Enter the string you want to input : ")
count = 1
for i in range(1,len(str_input)+1):
 
    count = count*i
print(count)