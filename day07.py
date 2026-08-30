
#create a empty dict and print its type
d = {}
print(type(d))
#create a empty set and print its type
s = set()
print(type(s))
#add 5 non-sequences and 6 sequences to that set with add method
s.add(5)
s.add(3.4)
s.add(True)
s.add((3+5j))
s.add(None)
s.add('abc')
s.add(range(1,4))
# s.add([1,2,3])    #error, set will not allow list
s.add((1,2,3))
# s.add({1,2,3})      #error, set will not allow set
# s.add({1:2, 2:4})   #error,m set will not allow dict
print(s)

#add 5 non-sequences and 6 sequences with update method
s = set()
# s.update(5)            #cannot add non-sequence int with update
# s.update(3.4)          #cannot add float with update
# s.update(True)         #cannot add True with update method
# s.update((3+5j))       #cannot add complex with update method
# s.update(None)         #cannot add None with update method
s.update('rak')
s.update(range(1,4))
s.update([1,2,3], (1,2,3))    
s.update((1,2,3))
s.update({1,2,3})   
s.update({1:2, 2:4})  
print(s)


#print a set and remove first element from that set
print(s)
s.pop()
print(s)
#remove one existing and one non-existing element from that set
s.remove('a')   
# s.remove('z')   #error, z is not present
print(s)
#discard one existing and one non-existing element from that set
s.discard('r')
s.discard('z')    #No error, even if z is not present
print(s)
#remove all elements from the set
s.clear()
print(s)

#create a set {1,2,3,4}, a list [3,4,5,6]. 
s = {1,2,3,4}
l = (3,4,5,6)
print(s)
print(l)
#write union of set and list
print(s.union(l))
#write intersection of set and list
print(s.intersection(l))
#write difference of set and list
print(s.difference(l))
#write symmetric difference of set and list
print(s.symmetric_difference(l))
#use union, intersection, difference, symmetric difference operators on set and another set. try to change second type of list and see outputs
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1 | s2 )
print(s1 & s2)
print(s1 - s2)
print(s1 ^ s2)


#DICT METHODS
#create a empty dict
d = {}

#update dict with another dict
d.update({1:'a', 2:'b'}) 
print(d)              
#update dict with another list
d.update([ [1,'a'], [2, 'b'], [3, 'c'] ])
print(d)
#update dict with another tuple
d.update( ( (4, 'd'), (5, 'e'), (6, 'f') )  )
print(d)
#update dict with another set
d.update({(7, 'a'),(8, 'b'),(9, 'c')})

#create a dict with {1:'a', 2:'b', 3:'c', 4:'d'}
d = {1:'a', 2:'b', 3:'c', 4:'d'}
#remove the pair with key 4
d.pop(4)
#remove the pair with key 100
# d.pop(100)       #error, 100 is not present in dict
#remove the pair with key 100 if not there return 'z'
d.pop(100, 'z')
#remove the last pair
d.popitem()
#remove all elements from the dict
print(d)
d.clear()
print(d)

#create a dict with {1:'a', 2:'b', 3:'c', 4:'d'}
d = {1:'a', 2:'b', 3:'c', 4:'d'}
#get the value of key 4
print(d.get(4))
#get the value of key 100
print(d.get(100))
#get the value of key 100, if key is not present get 'z'
print(d.get(100, 'z'))
print(d)

#get the value of key 4 with setdefault
print(d.setdefault(4))
print(d)
#get the value of key 100 with setdefault
print(d.setdefault(100))
print(d)
#get the value of key 101 with setdefault, if key is not there add 100 with 'z'
print(d.setdefault(101, 'z'))
print(d)

#get all keys of dict and print its type
a = d.keys()
print(type(a))
#get all values in dict and print its type
b = d.values()
print(type(b))
#get all items in dict and print its type
c = d.items()
print(type(c))
print()
print()
d = {1:'a', 2:'b'}
print(d)
d[3] = 'c'
print(d)
d[3] = 'd'
print(d)
print(d[3])
print(d)
del d[3]
print(d.get(3))
print(d)