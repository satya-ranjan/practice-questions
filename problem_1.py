# we need to write a program to find the total no. of "Uppercase" characters in the given string


def uppercase(str1):
    j=0
    for i in range(len(str1)):
        if str1[i]>= "A" and str1[i] <= "Z":
            j = j+1
    print(j)

str1=input("Enter the string : ")
uppercase(str1)

            