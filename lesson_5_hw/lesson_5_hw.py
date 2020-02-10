""" Homework 5 """

'''- Implement your own _map as a generator function
first arg is collection, second arg - callback (mapper)
function returns new collection of mapped items (lazy, by request).
Usage of standard map functionality is forbidden.
Print values using: next, loop'''


def _map(callback, collection):
    for i in collection:
        yield callback(i)


MAP_1 = _map(lambda x: x * x, [2, 4, 5])
print(next(MAP_1))
print(next(MAP_1))


'''- Implement your own _unique function using:
1)  dictionary comprehension.
2)  set comprehension
First arg is collection.'''


COLLECTION_1 = [2, 3, 3, 2, 1, 2, 3, 5, 4, 6]


def print_decorator(func):
    """

    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        print("start")
        returned_value = func(*args, **kwargs)
        print("end")
        return returned_value

    return wrapper


@print_decorator
def _unique_dict(collection):
    dict1 = {k: "value" for k in collection}
    print(list(dict1.keys()))


_unique_dict(COLLECTION_1)


def _unique_set(collection):
    set1 = {x for x in collection}
    print(set1)


_unique_set(COLLECTION_1)


'''- Create iterator from tuple which created using comprehension
print values using: next, loop'''

NEW_COLLECTION = iter(tuple(x for x in range(10)))
print(next(NEW_COLLECTION))

'''- Implement _print decorator. Decorator should print result of the decorated
function evaluation
Decorate _unique fn with this decorator.
unique items should be print automatically'''


def print_decorator_1(func):
    """

    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        returned_value = func(*args, **kwargs)
        print(returned_value)
        return returned_value

    return wrapper


LIST_1 = [1, 2, 3]
LIST_2 = [4, 5, 6]

TUPLE_1 = (*(x for x in LIST_1),)
print(type(TUPLE_1))
print(TUPLE_1)
ITER_1 = iter(TUPLE_1)
print(next(ITER_1))
