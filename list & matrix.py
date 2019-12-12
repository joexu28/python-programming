for item in "Python":
    print (item)
for item in ["joe", "John", "smith"]:
    print(item)
for item in range(5, 10):
    print(item)

total = 0
prices = [10, 20, 30]
for item in prices:
    total += item
print (f"Total: ${total}")

for x in range(3):
    for y in range(3):
        print (f"({x}, {y})")

numbers = [5, 2, 5, 2, 2]
for x in numbers:
    output=''
    for y in range(0, x):
        output += '*'
    print(output)
numbers = [5, 2, 5, 2, 2]
for x in numbers:
    output='*' * x
    print(output)

numbers = [2, 2, 2, 2, 5]
for x in numbers:
    output=''
    for y in range(0, x):
        output += '*'
    print(output)

## list
names = ['john', 'bob', 'mosh', 'sarah', 'Mary']
print(names[:4])

numbers = [5, 6, 10, 1, 30, 26]
largest_number = numbers[0]
for number in numbers[1:]:
    if largest_number <= number:
        largest_number = number
print(f"the largest number is: {largest_number}")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for column in row:
        print(column)

numbers = [5, 2, 7, 10, 20, 15]
numbers2 = numbers.copy()
numbers.append(30)
numbers.insert(0, 100)
numbers.remove(5)
numbers.pop()
numbers.sort()
numbers.reverse()
print(50 in numbers)
#print(numbers.index(100))
print(numbers)
print(numbers2)

number = [5, 2, 6, 9, 10, 5, 10]
uniques =[]
for item in number:
    if item not in uniques:
        uniques.append(item)
print(number)
print(uniques)

#tuple
numbers = (1, 2, 3)
print(numbers.index(1))