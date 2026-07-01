import pandas as pd


def func1():
    # tuples are immutable
    test = (1, 2, 3)

    print(test)
    test2 = test.__add__((666, 777))
    print(test)
    print(test2)
    pass


def func2():
    test = [1, 2, 3]
    test.append(666)
    print(test)


def product(*args: float):
    result = 1
    for num in args:
        result *= num
    return result


def sum(*args: float):
    result = 0
    for num in args:
        result += num
    return result


def printall(**kwargs: str) -> None:
    for i, (key, value) in enumerate(kwargs.items()):
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(i if i < 20 else i % 10, "th")
        print(f"The {i}{suffix} argument is {key} = {value}")
    pass


def test2():
    data = {"name": ["joe", "bob"], "role": ["admin", "readonly"]}
    df = pd.DataFrame(data)
    print(df)
    df.loc[df["role"] == "admin", "name"] = "The Big Kahuna"
    df.loc[df["role"] == "readonly", "name"] = "Les[s] (Nessman)"
    print(df)


if __name__ == "__main__":
    # main = "testing"
    # print(f"in the {main} function!")
    # result = sum(1, 2, 3, 4, 5)
    # print(result)
    # name = "pete"
    # printall(foo="bar", bazz="zorg", super="cala", fraga="listic", expi="aladocious")
    test2()
