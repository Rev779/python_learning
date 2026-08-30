#create a list with 3 elements
l = [1,2,3]
print(l)
print()
#INSERT OPERATIONS
#appending
#add 5 types of non-sequence elements to it with append
l.append(1)
l.append(2.3)
l.append((4+3j))
l.append(True)
l.append(None)
print(l)
print()
#add 5 types of sequences to it with append 
l.append('abc')
l.append(range(1,3))
l.append([1,2,3])
l.append((1,2,3))
l.append({1,2,3})
l.append({'a':1, 'b':2})
print(l)
print()
#extending
#add 5 types of non-sequence elements to it with extend
# l.extend(5)       #error, not a sequence
# l.extend(4.3)     #error, not a sequence
# l.extend((1+2j))  #error, not a sequence
# l.extend(True)    #error, not a sequence
# l.extend(None)    #error, not a sequence
# l.extend(1,2,3)   #error, takes only one argument

#add 5 types of sequence elements to it with extend
l.extend('abc')
l.extend(range(1,3))
l.extend([1,2,3])
l.extend((1,2,3))
l.extend({1,2,3})
l.extend({'a':1, 'b':2})
print(l)



#inserting
l = [1,2,3,4,5]
print(l)
#insert an element at index 1 and print
l.insert(1, 'rak')
print(l)
#insert an element at index -1 and print
l.insert(-1, 'rak')
print(l)
#insert an element at index 10000 and print
l.insert(1000, 'rak')
print(l)
#insert an element at index -10000 and print
l.insert(-1000, 'rak')
print(l)

#DELETE OPERATIONS
#create a list with 1,2,1,3,4,1
l = [1,2,1,3,4,1]
#pop element at index 3 and print element and list
a = l.pop(3)
print(a)
#pop last element and print element and list
a = l.pop()
print(a)
#remove first 1 from list and print element and list
a = l.remove(1)
print(a)
print(l)
#clear all elements in the list
l.clear()
print(l)

#UPDATE OPERATIONS
#create a list with 3,2,1,5,4 
l = [3,2,1,5,4]
#sort the list in ascending and print
l.sort()
print(l)
#create a list with 3,2,1,5,4 
l = [3,2,1,5,4]
#sort the list in descending and print
l.sort(reverse=True)
print(l)
#create a list with 3,2,1,5,4 
l = [3,2,1,5,4]
#reverse the list and print
l.reverse()
print(l)

#READ OPERATIONS
#create a list with 1,2,1,3,1, 2
l = [1,2,1,3,1,2]
#find count of 1 and 2 in list
print(l.count(1))
print(l.count(2))
#find index of 1 from start
print(l.index(1))
#find index of 1 from 2nd index
print(l.index(1,2 ))
#find index of 1 from 5th index
# print(l.index(1, 5))   #indexerror, one is not found from 5


#TUPLE
#create a tuple with 1,2,1,3,1, 2
t = (1,2,1,3,2)
#find count of 1 and 2 in tuple
print(t.count(1))
print(t.count(2))
#find index of 1 from start
print(t.index(1))
#find index of 1 from 2nd index
print(t.index(1, 2))
#find index of 1 from 5th index
# print(t.index(1, 5))   #index error, 1 is not found from 5