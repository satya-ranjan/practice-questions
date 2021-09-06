start = int(input())
end = int(input())
list1 = []
for i in range(start,end+1):
    list1.append(i)
for j in range(len(list1)):
    if list1[j] % 3 ==  0:
        print("Fizz")
    elif list1[j] % 5 == 0:
        print("Bizz")
    else:
        print(list1[j])
 