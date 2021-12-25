input1 = list(map(int,input().strip().split(" ")))[:2]
n = input1[0]
m = input1[1]
input2 = list(map(int, input().strip().split(" ")))[:n]
list2 = []
list1 = input1.sort()

for i in range(m-1):
    list2.append(list1[i])
    print(list1[i])

res = max(list2) - min(list2)
print(res)
