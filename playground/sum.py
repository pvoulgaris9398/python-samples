import sys

print(sys.getrecursionlimit())

"""Recursive Version"""


def sum1(n):
    if n == 0:
        return n
    else:
        return n + sum1(n - 1)


"""Tail-Recursive Version"""


def sum2(n, acc=0):
    if n == 0:
        return acc
    else:
        return sum2(n - 1, acc + n)


print(sum1(10))
print(sum2(1000))
