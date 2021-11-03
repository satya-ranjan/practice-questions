# Consecutive Prime Sum
'''
Q  Some prime numbers can be expressed as a sum of Consecutive prime numbers
->5 = 2+3
17 = 2+3+5+7
41 = 2+3+5+7+11+13
'''
input1 = int(input("Enter the range you want to take !!! "))
list1 = [] 
sum = 0
count = 0
for i in range(2,input1):
    if i == 2 or i == 3 or i == 5:
        list1.append(i)
        
    elif ((i%2) != 0) or ((i%3) != 0) or ((i%5) != 0):
    
        list1.append(i)
        print(i)
print(list1)
for j in range(1,len(list1)):
    if list1[i]/2 != 0 or list1[i]/3 != 0:
        sum = sum + list1[i]
if sum/2 != 0 or sum/3 != 0:
    count = count + 1
print(count)
