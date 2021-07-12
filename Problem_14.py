'''
Take a string as input separate all integer form it,Then all int only once and form a lahest even possible. 
print lagest even number possible and if the number cann't be made, then print -1.
input
-----
asdf@75483
output
------
87534

'''
import re
input_str = input()
digits = list(set(re.findall("\d",input_str)))
digits.sort()
digits.reverse()
Number = int("".join(digits))
if Number % 2 == 0:
    print(Number)
else:
    length = len(digits)
    for i in range(length-1, 0,-1):
        if int(digits[i]) % 2 == 0:
            a = digits[i]
            digits.remove(a)
            digits.insert(length-1,a)
            even = int("".join(digits))

            print(even)