#Random password generator
import random , string
characters= 'abcdfghjikmnlk#2&*()'
password=''
print(string.ascii_letters)
import string
n=int(input("Enter the length of password:"))
for i in range(n):
    password+=random,choice(characters)
    print(password)

    #ATM
    import getpass
    balance=0
    p1=int(getpass.getpass("Enter your password:"))
    p2=int(getpass.getpass("RE-enter your password:"))
    pin =None
    if p1==p2:
        pin=p1
        print("your pin is set sucessfully")
        match n:
            case 1:
                print(f' your account balance is {balance}')
                amount=int(input("Enter the amount you want to depisit:"))
                balance +=amount
                print(f' your account balance is {balance}')