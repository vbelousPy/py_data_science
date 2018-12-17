my_list = [(a, b, a * b) for a in range(1, 10) for b in range(1, 10)]
# print(str(my_list))

my_dict = {a[0]: [(b[1], b[2]) for b in my_list if b[0] == a[0]] for a in my_list}
for k, v in my_dict.items():
    for i in v:
        print("{}*{}={}".format(k, i[0], i[1]), end='; ')
    print("")

gen_1 = (i for i in range(11))
print(gen_1)
print(list(gen_1))
print(list(gen_1))
