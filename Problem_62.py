input1 = int(input())
input2 = list(map(int, input().strip().split(" ")))[:input1]

for i in range(len(input2)):
        if input2[i] < input2[i+1]:
            del input2[i+]
print(input2)