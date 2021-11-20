'''
Problem Statement – Vohra went to a movie with his friends in a Wave theatre and during  break time he
bought pizzas, puffs and cool drinks. Consider   the following prices : 

Rs.100/pizza
Rs.20/puffs
Rs.10/cooldrink
Generate a bill for What Vohra has bought.

Sample Input 1:

Enter the no of pizzas bought:10
Enter the no of puffs bought:12
Enter the no of cool drinks bought:5
Sample Output 1:

Bill Details

No of pizzas:10
No of puffs:12
No of cooldrinks:5
Total price=1290
'''
input1 = int(input("no. of pizzas : "))
input2 = int(input("NO of puffas : "))
input3 = int(input("No of cooldrinks : "))

pizzas = input1*100
puffs = input2*20
cooldriks =input3*5
sum1 = pizzas+puffs+cooldriks

print("sum of pizzas : ",pizzas)
print("sum of puffas : ",puffs)
print("sum of cooldrinks : ",cooldriks)
print(f"total bill {sum1}")