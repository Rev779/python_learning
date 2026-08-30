#important problems
#1. print numbers from 1 to 10 
for x in range(1,11):
    print(x,end='  ')
    print('\n \n')
list=[4,5,6,7,9,5,4,3,6,8,9]
#2. print even numbers from 5 to 30 and above list
for x in range (5,31):
    if x%2==0:
        print(x,end='')
        print('\n \n')
        for x in list:
            if x%2==0:
                print(x,end='')
                print('\n \n')
list=[3,5,7,9,4,6,7,3,2,4,6,8]
#3. print odd numbers from 5 to 30 and above list
for x in range (5,31):
    if x%2==1:
        print(x,end='')
        print('\n \n')
        for x in list:
            if x%2==1:
                print(x,end='')
                print('\n \n')

#4. print numbers divisible by 5 from 1 to 30 and above list
list=[3,2,7,9,8,5,10,14,15,20,19,25,29,30]
for x in range (1,31):
    if x%5==0:
        print(x,end='')
        print('\n \n')
        for x in list:
            if x%5==0:
                print(x,end='')
                print('\n \n')

#5. print numbers divisible by both 5 and 7 from 1 to 100 and above list
list=[5,7,9,10,14,15,19,21,37,42,54,40,90,35,70,45]
for x in range (1,101):
    if x%5==0 and x%7==0:
        print(x,end='')
        print('\n\n')
        for x in list:
            if x%5==0 and x%7==0:
                print(x,end='')
                print('\n,\n')
#6. sum of numbers from 10 to 25 and above list
sum=0
for x in range(10,26):
    sum+=x
print("Sum of numbers from 10 to 25:", sum)
print()
#7. multiplication table of a number 
n=int(input('Enter a number for multiplication:'))
for i in range (1,21):
    print(f'(n)x(i)=(n*i)')
    print()
#8. factorial 
n=int(input('Enter a number for factorial:'))

#9. fibonacci 
for i in range (5):
    print(a)
    a,b= b,a+b

#10. reverse a string

#11. count vowels in a string
s=input('Enter the total vowels in the string')

#12. count z's and y's in a string

#13. check whether a number is prime number or not
n=int