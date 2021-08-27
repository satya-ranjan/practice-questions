'''
The of the Copper ca

You are the salary and years of expe

when the lary of an

The stuft onto a single tege doing sof The sunt noe wil hes the salary of a g

The song N inen will the Expe

Output Formatl

Ce a sig fang number repoceming the most


Sample Inpur
3
3000 
5000
4000
3
5
2
Sample Output
12500.00
'''
def curren_salary(salary,year):
    print(salary)
    print(year)
    for k in range(len(salary)):
        for l in range(len(year)):
            if k == l & year[l] > 4 :
                salary[k] = salary[k] + salary[k]*0.1
    print(sum(salary))

salary = []
year = []
N = int(input("Enter the number of input you want to take : "))
for i in range (N):
    S = int(input("Enter the salary of the employee  : "))
    salary.append(S)
for j in range (N):
    Y = int(input("Enter the year of the employee : "))
    year.append(Y)
curren_salary(salary,year)