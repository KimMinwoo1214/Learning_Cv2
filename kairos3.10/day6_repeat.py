# #1
# original_list = [1, 3, 5, 7, 9]

# print(list(map(lambda x: x + 2, original_list)))

# #2
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(list(map(lambda x: x ** 2  if x % 2 == 1 else x, numbers)))

# #3
# words = ["apple", "banana", "kiwi", "orange", "grape"]

# print(list(filter(lambda x: len(x) > 5, words)))

# #4
# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]

# print(list(map(lambda x, y: x * y, list1, list2)))

# #5 
# f = lambda x: x ** 3
# number = 7
# print(f(7))

# #6
# list6 = [ 18, 12, 11, 19, 17, 13, 15]
# mean1 = sum(list6) / len(list6)
# classify_number = lambda x: f'{x} equal mean' if x == mean1 else f'{x} big' if x > mean1 else f'{x} small'

# print(list(map(classify_number, list6)))

# #7
# string_list = ["apple", "banana", "kiwi", "orange", "grape"]
# prefix = "fruit_"

# print(list(map(lambda x: prefix + x, string_list)))

#1
string_dict = {"apple": "red", "banana": "yellow", "kiwi": "brown", "orange": "orange", "grape": "purple"}
search_value = "brown"

print(dict(filter(lambda x:  x[1] == search_value, string_dict.items())))

#2
string_dict = {"apple": "red", "banana": "yellow", "kiwi": "brown", "orange": "orange", "grape": "purple"}

# print({key: value.upper() for key, value in string_dict.items()})
print(dict(map(lambda item: (item[0], item[1].upper()), string_dict.items())))

#3
string_dict = {"apple": "red", "banana": "yellow", "kiwi": "brown", "orange": "orange", "grape": "purple"}

# print({value: key for key, value in string_dict.items()})
print(dict(map(lambda item: (item[1], item[0]), string_dict.items())))

#4
string_list = ["apple", "banana", "kiwi", "orange", "grape"]
# string_list.reverse()
print(sorted(string_list, reverse = True))

#5
string_dict = {"apple": "red", "banana": "yellow", "kiwi": "brown", "orange": "orange", "grape": "purple"}
 
print(dict(sorted(string_dict.items(), key = lambda x: x[1])))
