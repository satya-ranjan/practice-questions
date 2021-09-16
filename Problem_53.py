def Transmit(input1):
    for i in reversed(range(len(input1))):
            if input1[i] == input1[i+1]:
                print(input1[i])
                 


input1 = input()
Transmit(input1)