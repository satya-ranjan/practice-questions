'''
Description: As a young jedi you must learn to converse with Yoda. You have found a simple rule that helps change a "normal" sentence into "Yoda talk". Take the first two words in the sentence and place them at the end. Write a program that uses this rule to change normal sentence into "Yoda talk".

Input:

Input consists of a string that you must change

into "Yoda talk". Assume that the maximum length of the string is 100:

Output:

Print the corresponding sentence in Yoda talk.

Sample Input:

I will go now to find the Wookiee

Sample Output:

go now to find the Wookiee I will
'''


def yoda(sentence):
    str = " "
    temp = sentence.split(" ")
    temp1 = temp[:2]
    temp2 = temp[2:]
    convert = temp2 + temp1
    print(str.join(convert))



sentence = input('Enter the Sentence : ') 
yoda(sentence)