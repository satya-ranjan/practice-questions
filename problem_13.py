'''
Statement:
----------

Input will be like 5624381275. Separate odd places integers = 6, 4, 8, 2, 5

You have to return a 4-digit OTP by squaring the digits. Digits according to
input are 6, 4, 8, 2, 5

square those number = 36,16,64,4,25

 the OTP to be returned is first four digits i.e. 3616

'''
input_num = input("Enter Some number: ")
list_oddnum = ""
sqare = ""


for i in range (1,len(input_num)):
    if  i % 2 != 0:
        sqare = int(input_num[i])**2
        list_oddnum += str(sqare)

print(list_oddnum[:4])