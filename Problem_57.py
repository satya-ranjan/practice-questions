
'''
Problem Statement: Find the 15th term of the series?

0,0,7,6,14,12,21,18, 28

Explanation:

In this series the odd term is increment of 7 (0, 7, 14, 21, 28, 35

and even term is a increment of 6 (0, 6, 12, 18, 24, 30 }
input1 = 0,0
input2 = 15
 
output = 49


'''

def findmissigterm(list1,input1):
    odd = list1[0]
    even = list1[1]
    list2 = [odd,even]
    new = odd
    new1 = even
    for i in range (input1):
         
        if  i%2 == 0:
            new = new + 6
            list2.append(new)
        else:
            new1= new1 + 7
            list2.append(new1)
    print(list2[input1])


list1 = list(map(int, input("Enter the term : ").strip().split(",")))
input1 = int(input("which term do you want to find : "))
findmissigterm(list1,input1)