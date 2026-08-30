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
    
