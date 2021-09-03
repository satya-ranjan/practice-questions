from Problem_14 import Number


'''
    magic Number
    ------------
'''
def magic(array,temp):
    for i in range(len(array)):
        j = i+1 
        for j in range (len(array)):
            if array[i] < array[j]:
                array[i],array[j]= array[j],array[i]
    print(array)
    print(temp)
    good = 0
    bad = 0
    for k in range(len(array)):
        for l in range(len(temp)):
            if k == l & array[k] == temp[l]:
                good = good+array[k]
            else:
                bad = bad+array[k]
    print( good - bad )



num = int(input("Enter the number of input you want to take : "))
array = list(map(int, input("Enter the numbers : ").strip().split(" ")))[:num]
temp = array[:]
magic(array,temp)