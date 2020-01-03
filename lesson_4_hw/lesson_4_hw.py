""" Homework 4 """
# - Implement your own _unique function.
#   first arg is collection.
#   function returns new collection of uniq items
#   Usage of Set, Counter data structures is forbidden.


def _unique(collection):
    uniques = []
    for item in collection:
        if item not in uniques:
            uniques.append(item)

    return uniques


# - Implement your own _filter function.
#   first arg is callback, second arg - collection.
#   function returns new collection of items for which callback function call
#   return true
#   Usage of standard filter function is forbidden.
#
#   list(filter(lambda x: x, [0,1,2,3])) -> [1,2,3]
#   _filter(lambda x: x, [0,1,2,3]) -> [1,2,3]


def _filter(callback, collection):
    filtered = []
    for item in collection:
        if callback(item):
            filtered.append(item)

    return filtered


# - Implement your own _map function.
#   first arg is collection, second arg - callback (mapper)
#   function returns new collection of mapped items.
#   Usage of standard map functionality is forbidden.
#
#   list(map(lambda x: x, [1,2,3])) -> [1,2,3]
#   _map([1,2,3], lambda x: x) -> [1,2,3]


def _map(collection, callback):
    mapped = []
    for item in collection:
        mapped.append(callback(item))

    return mapped


# - Implement your own _find function.
#   first arg is callback, second arg - collection.
#   function returns first item from collection for which callback function
#   call return true
#   Usage of standard filter function or yor own _filter is forbidden.
#
#   _find([1,2,3], lambda x: x == 2) -> None
#   _find([{'a': 0, 'b': 1}, {'a': 1, 'b': 2}],
#       lambda item: item.get('a', 0) > 0) -> {'a': 1, 'b': 2}


def _find(callback, collection):
    lookup = []
    for item in collection:
        if callback(item):
            lookup.append(item)
            break

    return lookup
