digit_to_char = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wzyz",
}


def letter_combinations(digits):
    if not digits:
        return []

    answer = []

    def dfs(start_index, path):
        if start_index == len(digits):
            answer.append("".join(path))
            return

        for char in digit_to_char[digits[start_index]]:
            path.append(char)
            dfs(start_index + 1, path)
            path.pop()

        dfs(0, [])

        return answer


def main():
    print("Phone Numbers")


if __name__ == "__main__":
    main()
