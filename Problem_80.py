'''
Problem Statement  – In a theater, there is a discount scheme announced where one gets a 10% discount
on the total cost of tickets when there is a bulk booking of more than 20 tickets, and a discount of 2%
on the total cost of tickets if a special coupon card is submitted. Develop a program to find the total
cost as per the scheme. The cost of the k class ticket is Rs.75 and q class is Rs.150. Refreshments can
also be opted by paying an additional of Rs. 50 per member.

Hint: k and q and You have to book minimum of 5 tickets and maximum of 40 at a time. If fails display “Minimum of 5 and Maximum of 40 Tickets”.  If circle is given a value other than ‘k’ or ‘q’ the output should be “Invalid Input”.

The ticket cost should be printed exactly to two decimal places.

Sample Input 1:

Enter the no of ticket:35
Do you want refreshment:y
Do you have coupon code:y
Enter the circle:k
Sample Output 1:

Ticket cost:4065.25
Sample Input 2:

Enter the no of ticket:1
Sample Output 2:

Minimum of 5 and Maximum of 40 Tickets

'''
import sys

def __init__(self,ticketamount) :
    self.ticketamount = ticketamount
    
def ticket(self,n,r,c,ci):
    if ci == "k":
        self.ticketamount = n*75
        print("k",self.ticketamount)
    elif ci == "q":
        self.ticketamount = n*150
        print("q",self.ticketamount)
    if r == "y":
        refreshment(n,r)

def refreshment(self,n,r):
    refreshmentAmount = n*50
    self.ticketamount = self.ticketamount +  refreshmentAmount
    print("fre" ,self.ticketamount)






NOtickets=int(input("Enter the Numbet of ticket : "))
if NOtickets < 5 or NOtickets > 40:
    sys.exit()
refreshment = input("DO you want refreshmet : ")
coupon = input("Do you have coupon code : ")
circle = input("Enter the circle : ")
ticket(NOtickets,refreshment,coupon,circle)