# it doest directed possible but using frozenset-> it immutable set
# A frozenset can be placed inside another set

a = frozenset([1,2])        # it does not have indexing number and it Unordered
b = frozenset([3,4,5,6])

c = {a,b}
print(c)