def foo():
    a, b = 0, 1
    while True:
        result = a
        a, b = b, a + b
        yield result


gen_1 = foo()
for i in range(20):
    print(next(gen_1), end="; ")
