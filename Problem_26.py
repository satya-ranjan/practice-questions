'''
Reverse digits

Reverse(D) to be the reversal of all digits in D.

For example, Reverse(349)=943, Reverse(93)=39, and Reverse(340) = 43. Amrit wants to go to the movies with Nayak on some day D satisfying psDsq, but he knows

he only goes to the movies on days he considers to be lucky, Nayak considers a day to be lucky if the absolute value of the difference between d and Reverse(d) is evenly divisible by s. Given p, q, and s, count and print the number of lucky days when Amrit and Nayak can go to

the movies.

Input Format

A single line of three space-separated integers describing the respective values of p, q, and s

Constraints.

1p,s.q 10000

Output Format Print the number of beautiful days in the inclusive range between p and q.

Sample Input

10 13 6

Sample Output

2
'''


def reverse_digit(digit_input):
    num = 0 
    count =0 
    str1=""
    p = digit_input[0]
    q = digit_input[1]
    r = digit_input[2]
    for i in range(p , q+1):
        num = i
        str1 = str(i)
        rev = int(str1[::-1])
        if (rev - num)%r == 0:
            count += 1 
    print(count)



digit_input = list(map(int, input("Enter 3 number :").strip().split(" ")))
reverse_digit(digit_input)