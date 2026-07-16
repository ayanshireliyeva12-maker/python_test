# task 1
numbers = [
    int(input("1 number: ")),
    int(input("2 number: ")),
    int(input("3 number: "))
]

numbers.sort()

numbers.pop(0)
numbers.pop(-1)

result = tuple(numbers)

print(result)

# task 2

numbers = [5, 8, 2, 1, 5, 9, 2, 6, 1, 8]

result = tuple(sorted(set(numbers)))

print(result)

# task 3

list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 7, 8, 9, 10]

mixed_list = list_1 + list_2

del mixed_list[:3]
print(mixed_list)

del mixed_list[-2:]
print(mixed_list)

# task 4

names = []

while True:
    name = input()

    if name == "stop":
        break

    names.append(name)

names = list(set(names))

print(names)
print(len(names))

# task 5

numbers = [12, 4, 8, 15, 20, 7, 10, 5]

even = []
odd = []

for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)

# task 6

import random

numbers = []

for i in range(10):
    numbers.append(random.randint(1, 100))

even = 0
odd = 0

for i in numbers:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print(numbers)
print(max(numbers))
print(min(numbers))
print(sum(numbers) / len(numbers))
print(even)
print(odd)

# task 7

t_1 = (1, 2, 3, 4)
t_2 = (5, 6, 7, 8)

l_1 = list(t_1)
l_2 = list(t_2)

l = l_1 + l_2
l.sort()

t = tuple(l)

print(t)

# task 8

numbers = list(range(1, 101))

five = []
left = []

for i in numbers:
    if i % 5 == 0:
        five.append(i)

    if i % 3 != 0:
        left.append(i)

result = tuple(left)

print(five)
print(result)

# task 9

data = [10, 3.5, "Hello", True, 25, False, "Python", 7]

integers = []

for i in data:
    if type(i) == int:
        integers.append(i)

print(integers)

