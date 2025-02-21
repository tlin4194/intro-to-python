# Prints positional arguments


def f(*args, **kwargs):
    print("Positional:", args, kwargs)


f(100, 50, 25)
