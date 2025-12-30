"""
A "greedy" algorithm makes locally optimal choices
Once a "choice" is made, it is not revisited

It is "short-sighted" and _may_ not always find the optimal solution

"""

"""
1 cent
5 cents
10 cents
25 cents
50 cents
"""


def make_change(target_amount):
    coins = [50, 25, 10, 5, 1]
    coin_count = 0
    values = []
    for coin in coins:
        while target_amount >= coin:
            target_amount -= coin
            values.append(coin)
            coin_count += 1

    return coin_count, values


def test0(target_amount):
    print(make_change(target_amount))


def main():
    test0(28)
    test0(82)


if __name__ == "__main__":
    main()
