def penalty(num_input,list1):
    for i in range(num_input):
        print(list1[i])





num_input = int(input("Enter the no. of input you want to take : "))
list1 = list(map(int, input("Enter the numbers separeted by  , :").strip().split(",")))[:num_input]
penalty(num_input,list1)