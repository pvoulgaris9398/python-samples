import csv


def compare(file1, file2):
    differences = []

    differences.append((file1[0], file2[0]))

    with open(file1, "r") as csv1, open(file2, "r") as csv2:
        reader1 = csv.reader(csv1)
        reader2 = csv.reader(csv2)

        for row1, row2 in zip(reader1, reader2):
            if row1 != row2:
                differences.append((row1, row2))

                return differences
