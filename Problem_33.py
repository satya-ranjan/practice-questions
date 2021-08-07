'''
Given an array A[] of N integers and an integer X. The task is to count all the triplets (i, j, k) where 1 Si≤jsk≤N which satisfies the below

conditions.

1.XSj-i and X≤k-j.
2. A[i], A[j] and A[k] are odd.

Example 1:

Input:

N = 4

X = 1 A[] = {1, 2, 3, 3}

Output: 1

Explanation: There is only 1 triplet: (i=1, j-3, k-4) which satisfies all conditions.

'''

def CountTriplets(arr , n ):
    count = 0
    for i in range(0,n):
        for j in range(i+1, n):
            for k in range(j + 1 , n):
                if(arr[k] < arr[i] and arr[i] < arr[j]):
                    count += 1
    print(count)

arr = [1,2,3,4]
n = 4
print(CountTriplets(arr,n))