def largest_digit(sub_bank: str) -> tuple[str]:
    b_max = "0"
    i_max = 0

    for i, battery in enumerate(sub_bank):
        if battery > b_max:
            b_max = battery
            i_max = i
        if battery == 9:
            break
    return (sub_bank[0:i_max], b_max, sub_bank[i_max + 1 :])


def solve3(line: str, k=2):
    print(line)


def solve2(line: str, k=12):
    joltage = ""
    start = 0
    for i in reversed(range(k)):
        value = max(line[start - i :])
        start = line.find(value, start) + 1
        joltage += value
    return joltage


def solve(banks: list[str], k=12):
    ans = 0
    for bank in banks:
        selected_batteries = []
        remaining_bank = bank
        while True:
            split_index = len(remaining_bank) - (k - len(selected_batteries)) + 1
            possible_batteries = remaining_bank[0:split_index]
            unselectable_batteries = remaining_bank[split_index:]
            _, b_max, remainder = largest_digit(possible_batteries)
            selected_batteries.append(b_max)
            remaining_bank = remainder + unselectable_batteries
            if len(selected_batteries) == k:
                break

        max_battery = "".join(selected_batteries)
        ans += int(max_battery)
    return max_battery


def test0():
    input = "811111111111119"
    k = 12
    result = solve3(input, k)
    print(f"Result: {result}")


def main():
    test0()


if __name__ == "__main__":
    main()
