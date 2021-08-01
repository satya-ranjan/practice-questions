'''
Example 1:

input1:7
input2:1,2,3,4,5,6,7
input3:2

Output:3,4,5,6,7,1,2

'''



def insert_num(list_input,inst_input):
    first_num = list_input[:inst_input]
    last_num = list_input[inst_input:]
    final_num = last_num + first_num 
    print(final_num)

num_input = int(input("Enter the number of input you want take : "))
list_input = list(map(int, input("Enter the number of input you want to take : ").strip().split(",")))[:num_input]
inst_input = int(input("Enter the number of input : "))
insert_num(list_input,inst_input)