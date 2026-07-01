"""
Get a list of characters
Construct a set of unique integers that represent the indices
    where our target value can be found => "target_indices"
Construct a list of tuples of K indices => "combos"
Count this list of tuples
Count of tuples where any element (index) is also found
    in our "target_indices" => "matches"
Ratio = count of "matches" (numerator) divided by
    count of "combos" (denominator)
Round to 12 decimal places
Todo: Handle denominator == 0, empty list, validate inputs, etc.
"""

from itertools import combinations

if __name__ == "__main__":
    K = 2
    s = "a a c d"
    data = s.split()
    target = "a"
    data = ["a", "a", "c", "d"]
    indices = [i for i, c in enumerate(data, 1) if c == target]
    combos = list(combinations([i for i in range(1, len(data) + 1)], K))

    target_indices = set(indices)
    matches = [
        combo for combo in combos if any(element in target_indices for element in combo)
    ]

    print(indices)

    print(data)

    print(combos)

    print(matches)

    print(round(len(matches) / len(combos), 12))
