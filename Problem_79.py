'''
Problem Statement – FOE college wants to recognize the department which has succeeded in getting the
maximum number of placements for this academic year. The departments that have participated in the
recruitment drive are CSE,ECE, MECH. Help the college find the department getting maximum placements.
Check for all the possible output given in the sample snapshot

Note : If any input is negative, the output should be “Input is Invalid”.  If all department has equal
number of placements, the output should be “None of the department has got the highest placement”.

Sample Input 1:

Enter the no of students placed in CSE:90
Enter the no of students placed in ECE:45
Enter the no of students placed in MECH:70
Sample Output 1:

Highest placement
CSE

Sample Input 2:

Enter the no of students placed in CSE:55
Enter the no of students placed in ECE:85
Enter the no of students placed in MECH:85
Sample Output 2:

Highest placement
ECE

MECH

Sample Input 3:

Enter the no of students placed in CSE:0
Enter the no of students placed in ECE:0
Enter the no of students placed in MECH:0
Sample Output 3:

None of the department has got the highest placement

Sample Input 4:

Enter the no of students placed in CSE:10
Enter the no of students placed in ECE:-50
Enter the no of students placed in MECH:40
Sample Output 4:

Input is Invalid

'''
import sys

def highest(CSE,ECE,MECH):
    if CSE == 0 and ECE == 0 and MECH == 0:
        print("None of the department has got the highest placement ")
        sys.exit()
    elif CSE < 0 or  ECE < 0 or MECH < 0:
        print("Input is Invalid")
        sys.exit()

    m = max(CSE,MECH,ECE)


    if (m == CSE):
        print("CSE")
    if(m == ECE):
        print("ECE")
    if(m == MECH):
        print("MECH")




CSE = int(input("Enter the no of students placed in CSE : "))
ECE = int(input("Enter the no of students placed in ECE : "))
MECH = int(input("Enter the no of students placed in MECH : "))
highest(CSE,ECE,MECH)