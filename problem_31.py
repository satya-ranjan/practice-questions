'''
Sample Input:
10

output:
5

Explanation:
10 -> 5 jump - 1
5 -> 4 jump - 2
4 -> 2 jump - 3
2 -> 1 jump - 1

'''
def jump(num):
    count = 0
    while num != 0:
        if num % 2 == 0:
            num = num // 2
            count = count +1
        else:
            num = num - 1
            count = count + 1
                
    print(count)

num = int(input("Enter the number : "))
jump(num)