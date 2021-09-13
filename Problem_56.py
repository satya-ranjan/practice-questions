'''
We want to estimate the cost of painting a property. Interior wall painting cost is Rs.18 per sq.ft. and exterior wall painting cost is Rs.12

per sq.ft.

Take input as

1. Number of Interior walls

2. Number of Exterior walls

3. Surface Area of each Interior Wall in units of square feet

4. Surface Area of each Exterior Wall in units of square feet

If a user enters zero as the number of walls then skip Surface area values as User may don't want to paint that wall. Calculate and display the total cost of painting the property

Example 1:

6
3
12.3
15.2
12.3
15.2
12.3
15.2
10.10
10.10
10.00

Total estimated Cost: 1847.4 INR

'''

def cost(inner,outer):
    sum_innre= 0
    sum_outer = 0
    if inner > 0:
        
        for i in range(inner):
            inner_wall_values = float(input("inner_wall_values : "))
            sum_innre = sum_innre + inner_wall_values
        mult_inner = sum_innre * 18
    if outer > 0:
        
        for j in range(outer):
            outer_wall_values = float(input("Outer_wall_Values : "))
            sum_outer = outer_wall_values + sum_outer
        mult_outer = sum_outer * 12
    print(mult_outer + mult_inner)




inner = int(input("inner : "))
outer = int(input("outer : "))
cost(inner,outer)