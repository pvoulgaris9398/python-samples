import inspect

"""
Simple example showing how to enumerate the methods on
a Python class in various ways
Adapted from: https://www.geeksforgeeks.org/python/how-do-i-get-list-of-methods-in-a-python-class/
Note, the example using `inspect` didn't print anything out,
so I modified it to look for `predicate=inspect.isfunction` and deconstruct the returned tuple
to get at the function/method name
"""


class MySampleClass:
    def method1(self):
        pass

    def method2(self):
        pass

    def method3(self):
        pass


def methods_via_dir(type):
    return [
        method
        for method in dir(type)
        if callable(getattr(type, method)) and not method.startswith("__")
    ]


def methods_via_inspect(type):
    return [
        (name) for (name, _) in inspect.getmembers(type, predicate=inspect.isfunction)
    ]


def methods_via_dict(type):
    return [
        method
        for method in type.__dict__
        if callable(getattr(type, method)) and not method.startswith("__")
    ]


def main():
    print("Methods using dir(): ", methods_via_dir(MySampleClass))
    print()

    print("Methods using __dict__ attribute: ", methods_via_dict(MySampleClass))
    print()

    print("Methods using `inspect` module: ", methods_via_inspect(MySampleClass))
    print()


if __name__ == "__main__":
    main()
