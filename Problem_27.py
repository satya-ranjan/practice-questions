'''
Write afunction to remove duplicat element from an array and return unique value only

sample input :10,10,11,12,12,13,13,13
sample output :10,11,12,13

'''

num = int(input("Enter the how many number you want to input : "))
list1 = list(map(int, input("Enter input separeted by , ").strip().split(",")))[:num]
print(set(list1))