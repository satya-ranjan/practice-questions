'''
Given a maximum of 100 digit number as input,find difference between the sm of odd and even
position digit

input = 4567
output = 2
'''



num = input("Enter the number")
i = 1
sum_even = 0
sum_odd = 0
differnce = 0
for i in range(len(num)):
    # num[i] = int(num[i])
    if i%2 == 0:
        sum_even += int(num[i])
    else:
        sum_odd += int(num[i])
differnce = sum_even - sum_odd
print(str(differnce)[1:])
'''
if differnce < 0:
    print(differnce*differnce - differnce )
else:
    print(differnce)
'''