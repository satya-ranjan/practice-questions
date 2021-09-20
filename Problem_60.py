'''
Problem Statement and casesProblem DescriptionA chocolate factory is packing chocolates into the 
packets. The chocolate packets here represent an array arrt of Nnumber of integer values. 
The task is to find the empty packets(0) of chocolate and push it to the end of the conveyorbelt(array).

For Example: N=7 and arr=[4,5,0,1.9,c ]). 
There are 3 empty packets in the given set. 
These 3 empty packets representedas O should be pushed towards the end of the array

InputOutput7- Value of N
4519500[4,5,0,1,0,0,5]
Element of arr[O] to arr[N-1],
While input each element is separated by newline

InputOutput6- Value of N
618200[6,0,1,8,0,2]
Element of arr[0] to arr[N While input each element is separated by newline

'''

input1 = int(input("Enter how many input you want : "))
input2 = list(map(int ,input("input are : ").strip().split(",")))[:input1]
new1 = []
new2 = []
for i in range(len(input2)):
    
    if input2[i] == 0:
        new1.append(str(input2[i]))
    else:
        new2.append(str(input2[i]))
sum = new2+new1
for j in range(len(sum)):
    print(int(sum[j]),end=",")


