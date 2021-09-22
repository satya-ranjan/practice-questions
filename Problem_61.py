'''
Problem Description

An English school teacher is teaching how to build sentences for kindergarten students. 
She starts by teaching two words in a sentence, then 3 words and so on. The next step is that she asks 
the students to find which word in the sentence they have made has the maximum number of alphabets. 
The task here is to write program to find the longest word in each input sentence(str). 
Note: The sentence can consist of uppercase, lowercase alphabets, special characters and numbers.

Input

Knowledge is the greatest gift

Output

Explanation

we can derive the word with highest number of characters is knowledge. Hence, output is 9.

Input

Output

11223##%U66778899 Saturn V rocket's first stage carries 203,400 gallons (770,000 litres) of kerosene fuel

19

Explanation

Longest word in the sentence is 11223##%U66778899 Hence, output is 19.
'''

input1 = input("This is locked : ")
list1= []
hig = []
ans = 0
list1 = input1.strip().split(" ") 
for i in range (len(list1)):
    hig.append(len(list1[i]))
for j in range(len(hig)):
    if ans < hig[j]:
        ans = hig[j]

print(ans)
