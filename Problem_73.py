''' 
Statement:

Given two numbers n1 and n2. Find prime numbers between n1 and n2, then make all possible unique 
combinations of numbers from the prime numbers list you found in step 1.

From this new list, again find all prime numbers. Find smallest (a) and largest (b) number from the
2nd generated list, also count of this list.

and 2nd nun Consider smallest and largest number as the 1st and 2nd number to generate Fibonacci
series respectively till the count (number of primes in the 2nd list).

Print the last number of a Fibonacci series as an output

Input Format:

One line containing two space separated integers n1 and n2.

Output Format:

number of a generated Fibonacci series.

Constraints:

2<=n1 and n2<=100 n2-n1 >= 35

Sample Input 1: 2 40

Sample Output 1: 13158006689

1st prime list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

Explanation for Test Case 1:

Combination of all the primes = [23, 25, 27, 211, 213, 217, 219, 223, 229,231, 32, 35, 37, 311, 313, 
319, 323, 329, 331, 337, 52, 53, 57, 511, 513, 517,519, 523, 529, 531, 537, 72, 73, 75, 711, 713, 717, 
719, 723, 729, 731, 737,112, 113, 115, 117, 1113, 1117, 1119, 1123, 1129, 1131, 1137, 132, 133,135, 137,
1311, 1317, 1319, 1323, 1329, 1331, 1337, 172, 173, 175, 177, 1711, 1713, 1719, 1723, 1729, 1731, 1737,
192, 193, 195, 197, 1911, 1913, 1917, 1923, 1929, 1931, 1937, 232, 233, 235, 237, 2311, 2313, 2317, 
2319, 2329, 2331, 2337, 292, 293, 295, 297, 2911, 2913, 2917, 2919, 2923, 2931,2937, 312, 315, 317,
3111, 3113, 3117, 3119, 3123, 3129, 3137, 372, 373,375, 377, 3711, 3713, 3717, 3719, 3723, 3729, 3731]

2nd prime list = [193, 3137, 197, 2311, 3719, 73, 137, 331,523,1931,719,337, 211, 23,1117, 223, 1123,
                229, 37, 293, 2917, 1319, 1129, 233, 173,3119, 113, 53, 373, 311, 313, 1913, 1723, 317]

smallest (a) = 23 largest (b) = 3719

Therefore, the last number of a Fibonacci series i.e. 34th Fibonacci number in the series that has 23 
and 3719 as the first 2 numbers is 13158006689
'''
list1 = []
list2 = []
list3 = []

def fibonacci(input1):
    first = input1[0]
    second = input1[1]

    
    for i in range(first,second):
        if prime(i) == True:
            list1.append(i) 
    crossjoin(list1)        

def prime(i): 
    for j in range(2,i):
        if i % j == 0:
            return False
    return True


def crossjoin(list1):
    for i in range(len(list1)):
        for j in range(len(list1)):
            if i!= j:
                list2.append(int(str(list1[i])+str(list1[j])))
    for i in range(len(list2)):
        if prime(list2[i]) == True:
            list3.append(list2[i])


            



input1 = list(map(int, input( ).strip().split(" ")))
fibonacci(input1)
print(list1)
print(list2)
print(list3)
