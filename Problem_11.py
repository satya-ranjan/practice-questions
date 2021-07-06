'''
A string of comma separated numbers ,the numbers 5 and 8 are present in the list(8 always comes after 5
Num1 : 
Add all members which  do not lie between 4 and 7(excluding 4,7)
Num2:
Number form by concanatic all numbers from 4 to 7(including 4,7)
Output
Num1+num2

Case 1:
Input =3,2,6,4,1,4,7,9
Output=5168
num1=3+2+6+9=20
num2='5'+'1'+'4'+'8'=5148
Output=5148+20=5168
Case 2:
Input:=4,1,5,7
Output =62
'''
num_list= input("Enter the string separeted by  , :").split(",")
length = len(num_list)

Index_4 = num_list.index("4")
index_7 = num_list.index("7")

num1 = 0
num2 = ""

for i in range (0 , length):
    if(i< Index_4 or i > index_7):
        num1  = num1 + int(num_list[i])
for i in range(Index_4 , index_7+1):
    num2 = num2 + num_list[i]

print( int(num2)+ num1 ) 