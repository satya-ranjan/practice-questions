

'''
Electrostatics

Doug is fond of change, every now and then he tries to do new things. This time, he caught up with a rod comprising of negative (N) and positive (P) charges. He is asked to calculate the maximum net electrostatic field possible in the region due to the rod

Note: Assume, Electrostatic Field Total charte 100

Input Specification:

input1: integer array denoting the magnitude of each charge input2: String denoting nature of each charge, entry represents a sign of

charge at location in input1 input3: No. of charges it holds (length of input1)

Output Specification:

Return the maximum electrostatic field possible in the rod

Example 1:

input1: 14.3.5)

inputz: PNP

input3: 3

'''
def electrostatic(input1,input2,input3):
    x = []
    add= 0
    input1 = input1[:input3]
    input2 = input2[:input3]

    for i in range(len(input1)):
        for j in range(len(input2)):
            if i == j and input2[j] == "P":
                
                x.append(input1[i])

            elif i==j and input2[j] == "N":
        
                x.append(-(input1[i]))
    

    print(sum(x)*100)



input1 = list(map(int , input("enter the input you want to take : ").strip().split(",")))
input2 = input("Entet P for +ve and n for -ve : ")
input3 = int(input("Enter how many input do you want to take : "))
electrostatic(input1,input2,input3)
