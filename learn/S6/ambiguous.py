def func(p1, p2, *args, k, **kwargs):
    print(f"positional-or-keyword:....{p1}, {p2}")
    print(f"var-positional (*args):...{args}")
    print(f"keyword:..................{k}")
    print(f"var-keyword;..............{kwargs}")


func(1, 2, 3, 4, 5, 9, k=6, key1=7, key2=8)

# As represented:

"""
1. Positional params (p1, p2)
2. Variable params (*args)
3. Keyword param (k)
4. Variable keyword params (**kwargs)
"""
