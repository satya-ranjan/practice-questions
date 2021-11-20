def Maxinum(input1):
    
    for i in range(input1):
        input2 = int(input("how many input you want to take : "))
        input3 = list(map(int, input("input are : ").strip().split(" ")))[:input2]
        count = 0
        list1 = []
    for j in range(len(input3)-1):
        k = j+1
        if input3[j] < input3[k]:
            print(input3[j],input3[k])
            count = count +1
        list1.append(input3[j])
    print(max(list1))
    
    print(max(list1)) 




input1 = int(input())
Maxinum(input1)

