with open("test1.csv", mode="r") as f1, open("test2.csv", mode="r") as f2:
    file1 = f1.readlines()
    file2 = f2.readlines()

with open("update.csv", "w") as outFile:
    for line in file2:
        if line not in file1:
            outFile.write(line)
