'''
You are given an array a comprising n integers. You have to calculate the magic value of the array a Magic value of an array is equal to the difference between the sum of good integers in an array and the sum of the bad integers in an array.

Good Integers are the ones whose indexes are not changed in an array when sorted, rest are bed

Input format

First line of Input contain a single integer n

Second line of input contain space separated integers, elements of array a
'''


def difference(num):
    good = 0
    bad = 0
    list1 = list(map(int, input("Enter the elements :").strip().split(" ")))[:num]
    temp = list1[:]
    for i in range(len(list1)-1):
        for j in range(len(list1)-1):
            if list1[j] > list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]
    
    for k in range (len(temp)):
        if temp[k] == list1[k]:
            good += list1[k]
        else:
            bad += list1[k]
    print(good - bad)


num = int(input("Entet how many input you want to input :"))
difference(num)
