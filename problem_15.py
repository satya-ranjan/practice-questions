'''
A non empty string input_str containg only brackest (,){,}[,] it return output_str based on following
  -input_str is properly nested ten return 0
  -input not properly nested, return position of element input_str - n+1
'''
from typing import Counter


string = input()
stack = []
Counter = 0
for a in string:
    if(a=="(" or a=="{" or a=="["):
        stack.append(a)
        Counter += 1
        continue

    if len(stack) == 0:
        print(Counter+1)
        exit()

    b = stack.pop()

    if(a=="]" and a == "["):
        Counter += 1
    elif(a=="}" and a=="{"):
        Counter += 1
    elif(a=="(" and a==")"):
        Counter +=1

    if(len(stack)==0):
        print(0)
    else:
        print(Counter+1)