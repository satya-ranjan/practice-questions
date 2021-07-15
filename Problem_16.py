'''
Take input form the use inthe given format(consist of name and code)

Find the maximum digit from code which is less then or equql to(<=) the length of name and put the place char in the final string if
thir is no any digit found which satisfies the given condition then simply put "x" 
'''
string_final = ""
string_input = input()
a = string_input.split(",")
for i in a:
    x,y = i.split(":")
    length = len(x)


    maximum = 0
    for j in y:
        if int(j) <= length and int(j) >=int(maximum):
            maximum = j
        
        if maximum == 0:
            string_final += "x"
        else:
            string_final += x[int(maximum)-1]
    print(string_final) 