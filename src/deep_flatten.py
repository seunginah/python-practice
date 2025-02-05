from typing import List
"""
https://www.pythonmorsels.com/exercises/05fe60de17824ef3ae77d93a3be2e98b/?level=advanced
In this exercise, we're going to work on flattening iterables. I'd like you to
write a function deep_flatten that accepts a list of lists (or lists of tuples
and lists) and returns a flattened version of that list of lists.

It should work like this:
deep_flatten([[(1, 2), (3, 4)], [(5, 6), (7, 8)]])
[1, 2, 3, 4, 5, 6, 7, 8]

deep_flatten([[1, [2, 3]], 4, 5])
[1, 2, 3, 4, 5]

In the examples above, we're returning a list. 
Your deep_flatten function should return an iterable, not necessarily a list.
"""

class DeepListIterator:
    """
    Iterate over a list  of lists, or list of tuples and lists
    """
    def __init__(self, l):
        self.l = l
        self.i = 0

    def __iter__(self):
        return self

    def recurse(self, x):
        return self.__next__(x)

    def __next__(self, l):
        if type(l) is list or type(l) is tuple:
            print(f"list/tuple: {l}")
            for i in range(len(l)):
                self.recurse(l[i])
        else:
            print(f"returning: {l}")
            raise StopIteration
            return l


def deep_flatten(l: List):
    """
    Args:
        l (): list - of lists, or tuples and lists

    Returns: DeepListIterator, an iterable over the flattened list
    """
    return DeepListIterator(l)

l1 = [[(1, 2), (3, 4)], [(5, 6), (7, 8)]]
for item in deep_flatten(l1):
    print(item)

# This works
def recurse(x):
    print("recurse")
    return iterate(x)

def iterate(l):
    if type(l) is list or type(l) is tuple:
        for i in range(len(l)):
            print(f"i: {i} \ttype: {type(l[i])}")
            recurse(l[i])
    else:
        print(f"l: {l}")
        return l

x = iterate(l1)