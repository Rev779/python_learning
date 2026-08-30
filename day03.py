#Operators
#Arithmetic Operators 
# + 
a = 5 + 7
print(a)
b = [1,2,3] + [4,5,6]
print(b)

# - 
a = 4 - 3 
print(a)
a = {1,2,3} - {2,3}
print(a)

#*
a = 5 * 6.0
print(a)
l = [1,2,3,4]
print(*l)
b = [1,2,3] * 4 
print(b)

#**
a = 2 **5
print(a)

#/
a = 5/2
print(a)

#//  : floor division or integer division
a = 5//2
print(a)
a = 5//2.0
print(a)

#%
a = 9 % 5 
print(a)




#Relational Operators 
a = 5 == 6
print(a)
a = 5 != 6 
print(a)
a = 5 > 6
print(a)
a = 5 >= 6 
print(a) 
a = 5 < 6 
print(a) 
a = 5 <= 6 
print(a)
#Tricky
a = 'aec' > 'adc'
print(a)

#Logical Operators
a = True and True 
print(a)
b = True and False 
print(b)
c = True or False 
print(c)
d = 1 or 0 
print(d)
e = '' and 'rak'
print(e)
f = False or 0 or []
print(f)
g = True and 1 and [1]
print(g)


#Assignemnt Operator
a = 100
a *= 34    
print(a)

#Walrus operator
a = 100            #assignment statement
print( a := 100)   #assign and return
print(a)


#Identity Operator : is
a = (1,2,3)
b = (1,2,3)
print(a is b)
a = [1,2,3]
b = [1,2,3]
print(a is b)
print(a == b)

#Membership operator : in 
a = 1 in {3,5,4}
print(a)