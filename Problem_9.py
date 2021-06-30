'''
    Password Validation
---------------------------

In this program, we will be taking a password as a combination of alphanumeric characters along with special characters, and check whether the password is valid or not with the help of few conditions.

Primary conditions for password validation :

Minimum 8 characters.
The alphabets must be between [a-z]
At least one alphabet should be of Upper Case [A-Z]
At least 1 number or digit between [0-9].
At least 1 character from [ _ or @ or $ ].
Examples:

Input : R@m@_f0rtu9e$
Output : Valid Password

Input : Rama_fortune$
Output : Invalid Password
Explanation: Number is missing

Input : Rama#fortu9e 
Output : Invalid Password
Explanation: Must consist from _ or @ or $

'''
def validation(s):
    flag = True
    secialchar= ["@","$","%"]

    if (len(s) < 8):
        print("The the Password should be more than 8 charater ")
        flag = False
    if not any(char.isupper() for char in s):
        print(" 1 upper case letter is requared")
        flag = False
    if not any(char.islower() for char in s):
        print("1 lower case letter is requared")
        flag = False
    if not any (char in secialchar for char in s):
        print("One secial charater is requared")
        flag = False
    if not any(char.isdigit() for char in s):
        print("one number shoudl required")
        flag = False
    if flag:
        return flag


def main():
    s = 'Geekggghhhhh@11'
      
    if (validation(s)):
        print("Password is valid")
    else:
        print("Invalid Password !!")
    
if __name__ == '__main__':
    main()
     
