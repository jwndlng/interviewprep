
def multi_yield():
    yield_str = "This will print the first string"
    yield yield_str
    yield_str = "This will print the second string"
    yield yield_str


def test():
    num = 0
    while True:
        yield num
        num+=1

multi_obj = multi_yield()
print(next(multi_obj))
print(next(multi_obj))

t = test()
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))