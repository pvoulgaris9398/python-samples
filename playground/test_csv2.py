import csv


def compare_csv(file1_path, file2_path, key_column, comparison_lambda):
    with open(file1_path, "r") as f1, open(file2_path, "r") as f2:
        reader1 = csv.DictReader(f1)
        reader2 = csv.DictReader(f2)

        data1 = {row[key_column]: row for row in reader1}
        data2 = {row[key_column]: row for row in reader2}

        unique_to_file1 = []
        unique_to_file2 = []
        changed_rows = []

        for key, row1 in data1.items():
            if key not in data2:
                unique_to_file1.append(row1)
            else:
                row2 = data2[key]
                if not comparison_lambda(row1, row2):
                    changed_rows.append({"file1_data": row1, "file2_data": row2})

        for key, row2 in data2.items():
            if key not in data1:
                unique_to_file2.append(row2)

    return unique_to_file1, unique_to_file2, changed_rows


def comparison_logic(r1, r2):
    r1["FIELD1"] == r2["FIELD1"]


file1_unique, file2_unique, changed = compare_csv(
    "test1.csv", "test2.csv", "RECORDID", comparison_logic
)

print(file1_unique)
print(file2_unique)
print(changed)
