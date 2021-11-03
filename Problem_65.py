input1 = int(input("Enter the input : "))
for i in range(input1,0,-1):
    for j in range(0,input1-i):
        print(end = " ")
    for j in range(0,i):
        print("*",end=" ")
    print()
  