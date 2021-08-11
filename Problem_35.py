
def secret (num):
    add1 = 0
    for i in range(len(num)):
        add1 = bin(add1 + num[i])
        print(add1)




num = []
input_num = int(input("Enter the number you want to take : "))
for i in range (input_num):

    nums_input = int(input("Enter the input numbers : "))
    num.append(nums_input)

secret(num)