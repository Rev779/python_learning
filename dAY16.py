#palindrome for number
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
#palindrome for string
n=int(input('Enter a string to check palindrome'))
temp =abs(n)
while n>0:
    s = s.lower().replace(" ", "")
    s == s[::-1]
    
    #Write a function to check prime number
    if n%2==0:
        for x in range(1,n):
            print(x,end ='')
            if n%2==0:
                print('Prime number')
            else:
                print('Not prime number')
                #Write function to check reverse string:
                def reverse_string(s):
                    return s[::-1]
