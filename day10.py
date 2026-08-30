list = [0,1,2,3,4]
# print elements in list with for each loop
print("For each loop:")
for num in list:
    print(num)

# print elements in list with index based for loop
print("\nIndex based for loop:")
for i in range(len(list)):
    print(list[i])

# skip printing even numbers in list
print("\nSkip even numbers:")
for num in list:
    if num % 2 == 0:
        continue
    print(num)

# skip printing odd numbers in list
print("\nSkip odd numbers:")
for num in list:
    if num % 2 != 0:
        continue
    print(num)

# when number 2 comes stop printing
print("\nStop when 2 comes:")
for num in list:
    if num == 2:
        break
    print(num)

# when first odd number comes stop printing
print("\nStop at first odd number:")
for num in list:
    if num % 2 != 0:
        break
    print(num)

# print numbers from 1 to 10, when all numbers are printed, print 'All numbers printed'
print("\n1 to 10:")
for num in range(1, 11):
    print(num)
else:
    print("All numbers printed")

# print numbers from 1 to 10, skipping even numbers, when all numbers are printed, print 'All numbers printed'
print("\n1 to 10 skipping even numbers:")
for num in range(1, 11):
    if num % 2 == 0:
        continue
    print(num)
else:
    print("All numbers printed")

# print numbers from 10 to 1, when 5 comes stop printing, when all numbers are printed, print 'All numbers printed'
print("\n10 to 1, stop at 5:")
for num in range(10, 0, -1):
    if num == 5:
        break
    print(num)
else:
    print("All numbers printed")