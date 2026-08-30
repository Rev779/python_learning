
#right angle triangle
# n = int(input('Enter any integer number:  '))
n = 4
for i in range(1, n+1):
    print(i * '*')
print()
#inverted right angle triangle
for i in range(n, 0, -1):
    print(i * '*')
print()
#pyramid
for i in range(1, n+1):
    print( (n-i)*' ' + i*'* ' )
#inverted pyramid
for i in range(n, 0, -1):
    print( (n-i)*' ' + i*'* ' )
print()
#hollow sqare
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 or i == n or j == 1 or j == n:
            print('*', end='')
        else:
            print(' ', end='')
    print()
#star (zero based indexing)
for i in range(n):
    for j in range(n):
        if i == n//2 or j == n//2 or i == j or j == n-i-1:
            print('*',end='')
        else:
            print(' ',end='')
    print() 

#NUMBER PATTERNS
#number right angle
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
print()
#number inverted right angle
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
print()
#same row pattern
for i in range(1, n+1):
    for j in range(i):
        print(i, end=' ')
    print()
print()
#inverted same row pattern
for i in range(n, 0, -1):
    for j in range(i):
        print(i, end=' ')
    print()
print()
#1's  pattern
for i in range(1, n+1):
    for j in range(i):
        print(1, end=' ')
    print()
print()
#inverted 1's  pattern
for i in range(n, 0, -1):
    for j in range(i):
        print(1, end=' ')
    print()
print()
#reverse number pattern
for i in range(1, n+1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()
print()
#number pyramid
for i in range(1, n+1):
    print((n-i)*' ', end=' ')
    for j in range(1, i+1):
        print(j, end=' ')
    print()
#reverse number pyramid
for i in range(n, 0, -1):
    print((n-i)*' ', end=' ')
    for j in range(1, i+1):
        print(j, end=' ')
    print()
print()
#pascal's triangle
for i in range(n):
    num = 1 
    for j in range(i+1):
        print(num, end=' ')
        num = num * (i-j) // (j+1)
    print()