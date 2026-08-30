#day2
print('Non-Sequences:')
#1. int
a = 2334   #without point
print(type(a))
#2. float  #with point
b = 2.41
print(type(b))
#3. complex
c = 3+4j
print(type(c))
#4. bool
d = False
print(type(d))
#5. NoneType
e = None 
print(type(e))
print()
print()
print('Sequences:')
l = [1,2,3,4]
print(type(l))
t = (1,)
print(type(t))
s = {1,2,3}
print(type(s))
f = frozenset({1,2,3})
print(type(f)) 
d = {'a':1, 'b':2, 'c':3}
print(type(d)) 
s1 = 'rakesh'
s2 = "rakesh"
s3 = '''ra
      kes
h'''
print(type(s1))
# print(type(s2))
# print(type(s3))
r1 = range(1,10,2)
# print(*r1)
r2 = range(10, 1, -2)
# print(*r2) 
print(type(r2))
print()
print()
print('Type Conversion: ') 
l = list( '1,2,3' )
print(l)