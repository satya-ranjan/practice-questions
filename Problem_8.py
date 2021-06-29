'''
Tom has an array of distinct integars 'a1', 'a2', 'a3', 'a4',....., 'an' of size 'n'.

Tom defines that value of a subset of array 'a' is maximum number in

that subset.

Calculate product of values of all possible non-empty subsets of array'a'.

Input Format

First line contains n (Number of elements in an array).

Next n lines contain n distinct integars a1, a2, a3, a4, ....... an.

Output Format

Print the answer % 1000000007

Constraints

1 <= n <= 10^3

1 <= ai <= 100 All al and aj are pairwise distinct (i = }}

Sample Example 1:

Input

2

3

7

Output

1

Explanation

vall (3))=3

vall (3.7) 1-7 answer=13*77) 147 1000000007 = 147
'''
def maxnumber( n,list1):
    m=max(list1)
    product = 1
    for i in range(n):
        if i < n:
            product = product*list1[i]
    print((product*m) % 1000000007)


n = int(input("Enter the number of items: "))
list1 = list(int(n) for n in input("\nEnter the numbers : ").strip().split())[:n]
maxnumber(n,list1)


