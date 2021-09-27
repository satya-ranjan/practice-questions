input1 = int(input())
input2 = int(input())
list1 = list(map(int, input().strip().split(" ")))[:input1]
sum = 0

for i in range(len(list1)):
    sum = sum + (int(list1[i]/input2))

print(sum)