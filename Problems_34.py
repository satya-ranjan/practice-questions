'''
'''
def divide1(input1):
    tot_num = input1[0]
    to_div = input1[1]
    index_count = input1[2]
    input_arr = list(input("Enter the numbers : "))[:tot_num]

    x = [input_arr[i:i + to_div]for i in range(0, tot_num,to_div)]
    print(x[0])
    
    










input1 = list(map(int, input("Enter the three input : ").strip().split(" ")))
divide1( input1 )
