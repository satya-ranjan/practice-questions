Total_candies = 10
K=0
def cadies_needed(Num):
    if Num == 0:
        print("invalid input")
    elif (Num >= 5):
        print("Invalid code:")
    else:
        print("Number of candied sold:",Num)
        K = Total_candies - Num
        print("Number of candies Left:",K)

number = int(input("Enter the no of candied you wants:"))
cadies_needed(number)








cadies_needed(int(input("Enter the number of Candies you want"))) 