"""
0 1 2 3 4 5 6

1 2 2 2 3 1 1

i   j   j-1
0   1   1       => j-i, s[i]    => (1, 1)
1   2   1
1   3   2
1   4   3       => j-i, s[1]    => (3, 2)
4   5   1
4   6   1       => j-i, s[1]    => (3, 1)
5   7   2       => j-i, s[1]    => (2, 1)
*

i=0,j=0,1=1
i=0,j=1,1<>2 no -> output
i=1,j=1,2=2
i=1,j=2,2=2
i=1,j=3,2=2
i=2,j=4,3 <> 2 no -> output
i=4,j=5,1 <> 2 no -> output
i=5,j=6,1=1
i=6,j=7,1=1 -> output last result to cover last record

"""


def myfunc(s: str):
    i = 0  # slow pointer
    j = 0  # fast pointer
    n = len(s)  # total characters

    if not s:
        return

    output = ""
    while i < n and j < n:
        if s[i] == s[j]:
            j += 1
        else:
            output += f"({str(j - i)}, {str(s[i])}) "
            i = j

    output += f"({str(j - i)}, {str(s[i])})"

    print(output)


if __name__ == "__main__":
    myfunc("1222311")
