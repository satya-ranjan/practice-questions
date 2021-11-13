'''
Statement: Little Jill jumbled up the order of the letters in our dictionary. Now, Jack uses this list 
to find the smallest lexicographical string that can be made out of this new order. Can you help him?

You are given a string P that denotes the new order of the letters in the English dictionary.
You need to print the smallest lexicographic string made from the given string S.

Constraints:
1 <= T <= 1000
Length * (P) = 26
1 <= length(S) <= 100
All character in the string S, P are in lower case
Input:
2
polikujmnhytgbvfredcxswqaz
abcd
qwryupcsfoghjkldezvxbintma
edoc

Input Format:
The first line contains number of
test cases T
The second line has the string P
The third line has the string S
Output Format:
Print single string in a new line for every test case giving the result

Output:
bdca
codevita
Subscribe
'''
input1 =  int(input("How many string you want to input : "))
for i in range(input1):
    P=input()
    S = input()
list1 = ""
for i in range(0,len(P)):
    if P[i] in S:
        list1 = list1+P[i]
print(P)
print(list1)
