some_list = list(range(1, 11))
print(some_list)
some_dict = dict()

result = 0
for i in some_list:
    result += i
some_dict.update({"1": result})

result = 1
for i in some_list:
    result *= i
some_dict.update({"2": result})

result = 1
for i in some_list:
    if i % 2 == 0:
        result *= i
some_dict.update({"3": result})

result = list([i ** 2 for i in some_list])
some_dict.update({"4": result})

print(str(some_dict))
