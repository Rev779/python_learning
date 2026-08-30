#While loop:
n=5
while n>=0:
    print('HI')
    print('Bye')
    print('Outside')

    n=5
while n>=0:
    print('HI')
    print('Bye')
    n -=1
    print('Outside')

    n=5
    while n<=10:
        print (n,end="")
        n+=1
        print('outside')

        n=5
        while n<=10:
            if n==7:
                continue
            print(n,end='')
            n+=1
        else:
            print('Loop sucessful;')
n=5
while n>=0:
    if n==3:
        break
    print(n,end='')
    n-=1
else:
    print('Loop sucessful')
print()

#print 1 to 10 with while loop
n=1
while n<=10:
    print(n,end='')
    n+=1
    #print even numbers from 1 to 10
    n=2
    while n<=10:
            print(n,end='')
            n+=2
            print()
            #print  numbers divisible by both 5 and 7 from 1 to 500
            n=1
            while n<=500:
                if n %5 ==0 and n %7==0:
                    print(n,end ="")
n+=1
print()
#count digits
n=input('Enter  the number to count digits:')
count=0
while n>0:
    n=n//10
    count+=1
    print('f Number of digits in the given number is:{count}')

    #reverse a number
    n=int(input('Enter number to reverse:'))
    temp=abs(n)
    while n> 0:
        last_digit =n%10
        rev = rev*10 + last_digit
        temp//=10
        if n<0:
            rev =-rev
            print('f Reverse of the given number is(rev)')


#palindrome
n=int(input('Enter a number to check palindome'))
temp =abs(n)
while n>0:
    last_digit=n%10
    rev=rev*10 + last_digit
    temp//=10
    if n<0:
        rev=-rev
        if rev ==n:
            print('Palindrome')
        else:
            print('Not palindrome')
