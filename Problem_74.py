list1 = []
def factors(input1):
    N = input1[0]
    k = input1[1]
    for i in range(1,N):
        if N%i == 0:
            list1.append(i)
    kth(list1)


def kth(list1):
    for i in range(len(list1),1,-1):
                print(list1[i])
                

input1 = list(map(int, input("Write two input separeted by , :").strip().split(",")))
factors(input1)