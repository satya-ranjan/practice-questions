'''
Here you are given unbiased dice containing 6 faces. You will be given an output sum which should
be obtained by throwing two dice. You need to return the number of all possibilities where the sum 
on both the dice is equal to the output sum. If there are no possibilities return 0.

Input

10

Output

3

'''
dice1 = [1 , 2 , 3 , 4 , 5 , 6]
dice2 = [1 , 2 , 3 , 4 , 5 , 6]
input_num = int(input("Enter the input you want to take : "))
count = 0
for i in range (len(dice1)):
    for j in range(len(dice2)):
        if (dice1[i] + dice2[j]) == input_num:
            count = count + 1
print(count)