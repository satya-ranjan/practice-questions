'''
You have to travel to different villages to make some profit.
In each village, you gain some profit. But the catch is, from a particular village i, you can only move to a village j if and only if  and the profit gain from village j is a multiple of the profit gain from village i.

You have to tell the maximum profit you can gain while traveling.

Input format

The first line contains a single integer N denoting the total number of villages.
The second line contains N space-separated integers, each denoting the profit gain  from village i.
Output format

Print the maximum profit you can gain.

Sample Input
6
1 2 3 4 9 8
Sample Output
15
'''




def Profit(list_num):
    add = 0 
    for i in range (len(list_num)):
        for j in range(len(list_num)):
            if list_num[i]<list_num[j]:
                print("grater",list_num[i])
                if list_num[i]*2 == list_num[j]:
                    #print("Multiple",list_num[i])
                    add = add + list_num[j] 
                    #print("add",count)
    print("ans",add)


num = int(input("Enter how many input you want to take : "))
list_num = list(map(int , input("Enter thr input you want to take : ").strip().split(" ")))[:num]
Profit(list_num)