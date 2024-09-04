numbers = (1, 2, 3, 4, 5)
print(*numbers, sep=";")

# operator packs everything into a tuple


def test_star(*args):
    print(args)
    for x in args:
        print(x)


print()

# test_star(0, 2, 4, 6)
test_star(2, 3, 4)
