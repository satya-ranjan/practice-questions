'''
Given a array of size n, write a funtion rearrange the numbers of the array in such a way that 
even and odd numbers are arranged alternatively in increasing order

input 1:- Array size i.e n
input 2:- Array elements (separated by comma)

Example 1 :
input 1:- 5
input :- (9,12,23,8,5)

Output: (5,8,9,12,23)

'''
def odd_even(list1):
    l1=[]
    l2=[]
    for i in range(len(list1)):
        if list1[i]%2 == 0:
            l1.append(list1[i])
        else:
            l2.append(list1[i])
            

num = int(input("Enter the no of array you want to input : "))
list1 = [int(input("enter the Number : "))for i in range(num)]
print(list1)

odd_even(list1)

