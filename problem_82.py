import re


regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isValid(input1):
    output1 = ''
    if re.fullmatch(regex, input1):
        for i in range(len(input1)):
          if input1[i] == "@":
              for j in range(i,len(input1)):
                  output1 = output1 + input1[j]  
        print((output1)[1::])
    else:
      print("invalid email")
input1 = input()
isValid(input1)