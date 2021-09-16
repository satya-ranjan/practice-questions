'''
A high-profile secret agency wants to handle all the messages sent and received in ciphers. They need to build a program/software where every mail sent or received in the organization will be encrypted using some secret codes. One of formats used can be as follows:

Actual

Cipher

9

h

m

Actual

m

P

Cipher

P

V

Actuals

Cipher x



b
2

d

e

The task is to encrypt the given string(str1) as per the ciphers given in the format above. Note: 
String cannot have any special characters, space, number or any uppercase latter.
'''

input1 = input("Enter the input you want to take : ")
output2 = ""
for i in range (len(input1)):
    
    if input1[i] <= chr(117):
        output2 =output2+ chr(ord(input1[i]) + 5)
    else:
        output2 =output2 + chr(ord(input1[i])-21)
print(output2)
    
        
