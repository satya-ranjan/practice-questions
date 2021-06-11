''' The followig letter of english alphabet are vowels: a,e,i,o,u.
    you are given a function
    def findMostFrentVowel(str)

    input:
    abeaicaidao

    Output:
    a
'''



def FindMostfrequentVowel(str):
    a=0
    e=0
    i=0
    o=0
    u=0
    for vowel in range(len(str)):
        if str[vowel]== "a" or str[vowel] == "A":
            a=a+1
        elif str[vowel]== "e" or str[vowel]== "E":
            e=e+1
        elif str[vowel]== "i" or str[vowel]== "i":
            i=i+1
        elif str[vowel]== "o" or str[vowel]== "O":
            o=o+1
        elif str[vowel]== "u" or str[vowel]== "U":
            u=u+1

    if (a>e) and (a>i) and (a>u) and (a>o):
        print("a")
    elif (e>a) and (e>i) and (e>u) and (e>o):
        print("e") 
    elif (i>e) and (i>a) and (i>u) and (i>o):
        print("i") 
    elif (o>e) and (o>i) and (o>u) and (o>a):
        print("o") 
    elif (u>e) and (u>i) and (u>o) and (u>a):
        print("u") 
    
n=input("Enter the string:")
FindMostfrequentVowel(n)




