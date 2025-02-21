def square(x):
    return x*x


original = {1, 2, 3, 4}
new_l = map(square, original)
print(list(new_l))


def is_odd(x):
    return x % 2 == 1


odd_nums = list(filter(lambda x: x % 2 == 1, original))
print(odd_nums)
