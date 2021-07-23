'''
One programming language has folling kayword that cannot be used as identifiers

break,case,continue,default,defer,else,for,func,goto,if,map,range,return,struct,type,var

input = for

output = for is a keyword

'''
key_word = ["break","case","continue","default","defer","else","for","func","goto","if","map","range","return","struct","type","var"
]
inputkey_word = input("Enter the keyword You want to input : ")

if inputkey_word in key_word:
        print(inputkey_word,"is a keyword")
else:
        print(inputkey_word,"is not a keyword")
