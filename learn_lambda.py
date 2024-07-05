# f = lambda x, y: [i for i in range(x, y)]

# print(f(1, 11))

# list1 = list(map(lambda x: x, range(11)))
# print(list1)

# even_numbers = list(filter(lambda x: x % 2 == 0, list1))
# even_numbers1 = [i for i in range(11) if i % 2 == 0]
# print(even_numbers)
# print(even_numbers1)

# ex = lambda x, y: [x[i] + y[i] for i in range(len(x))]

# list5 = list(map(lambda x,y: x + y, even_numbers, even_numbers1 ))
# print(list5)

# maxval = lambda x, y: x if x > y else y

# print(maxval(6, 10))

original_list = [1, 3, 5, 7, 9]

print(list(map(lambda x: x + 2, original_list)))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(map(lambda x: x ** 2 if x % 2 == 1 else x, numbers)))

words = ["apple", "banana", "kiwi", "orange", "grape"]
print(list(filter(lambda x: len(x) > 5, words)))

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
print(list(map(lambda x, y: x * y, list1, list2)))

f = lambda x : x ** 2 if x % 2 == 0 else x ** 3

print(f(7))

numbers = list(range(11))  
classify_number = lambda x: '0' if x == 0 else 'Odd' if x % 2 != 0 else 'Even'

classified_numbers = list(map(classify_number, numbers))

for num, classification in zip(numbers, classified_numbers):
    print(f"Number {num} is {classification}")