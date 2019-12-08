'''- Create tuple with chars from a long string.
  Slice last 20 chars in reversed order beging from 5th (5th from end).
  Create dictionary from sliced chars. Print sorted keys of this dictionary.'''
my_tuple = tuple("The way to get started is to quit talking and begin doing.")
'''('T', 'h', 'e', ' ', 'w', 'a', 'y', ' ', 't', 'o', ' ', 'g', 'e', 't', ' ',
's', 't', 'a', 'r', 't', 'e', 'd', ' ', 'i', 's', ' ', 't', 'o', ' ', 'q', 'u',
'i', 't', ' ', 't', 'a', 'l', 'k', 'i', 'n', 'g', ' ', 'a', 'n', 'd', ' ', 'b',
'e', 'g', 'i', 'n', ' ', 'd', 'o', 'i', 'n', 'g', '.')'''

sliced = my_tuple[-5:-25:-1]
'''('o', 'd', ' ', 'n', 'i', 'g', 'e', 'b', ' ', 'd', 'n', 'a', ' ', 'g', 'n',
'i', 'k', 'l', 'a', 't')'''

unique = set(sliced)
# {'t', 'g', 'd', 'l', 'i', 'a', ' ', 'k', 'o', 'e', 'n', 'b'}

my_dict = {}.fromkeys(unique)
'''{'t': None, 'g': None, 'd': None, 'l': None, 'i': None, 'a': None, ' ': None,
 'k': None, 'o': None, 'e': None, 'n': None, 'b': None}'''

print(sorted(my_dict))
# [' ', 'a', 'b', 'd', 'e', 'g', 'i', 'k', 'l', 'n', 'o', 't']


'''- Create list of chars from a long string. Extend list by chars from another
string. Remove duplicated items form list. Delete middle element using slice
functionality (important).'''
list1 = list("Anything that can go wrong ")
list2 = list("will go wrong!")

list1.extend(list2)

unique = set(list1)
unique = list(unique)
print(unique)

final = unique[:((len(unique)//2)-1)] + unique[(len(unique)//2):]

# index = (len(unique)//2)-1
# print(index)

# final = unique[:index] + unique[(index + 1):]

print(final)


'''- Create set with any elements. Create dictionary from this enumerated
set.'''
my_set = \
    {"name", "formula", False, ("C", "H", "O", "N"), "SI", 2, False, 0.0001}
enumd = enumerate(my_set)
# print(type(enumd))

my_dict = dict(list(enumd))
print(my_dict)


'''- Create two Sets with numbers and chars. Find intersection, union,
difference between them.
Use difference_update to update one set by other.'''
set1 = {"f", 9, 32, 5, 6, 23, "h", 90, "v", "o", "w"}
set2 = {"90", "v", 9, 32, 76, "p", "m"}

# intersection
interset = set1 & set2
print(interset)

# union
uniset = set1 | set2
print(uniset)

# difference
diffset = set1 - set2
print(diffset)

# symmetric difference
symdiffset = set1 ^ set2
print(symdiffset)
