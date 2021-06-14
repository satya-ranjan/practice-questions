'''
Given an array of A[] and positive integer K,the task is to count total number of pairs in the 
array whose sum is divisible by K
Eg
Input: A[] = {2,2,1,7,5,3}
output: 5
'''
def sumDivisibleByK(a,k):
    count=0
    for i in range(len(a)):
        for j in range(len(a)):
            if i<j:
                sum = a[i]+a[j]
                if sum%2 == 0:
                    count =count+1
    print(count)
A =[1,2,3,4,5]
n=3
sumDivisibleByK(A,n)

            
