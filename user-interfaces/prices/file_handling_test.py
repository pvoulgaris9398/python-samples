import json

import file_handling


def save_data(file_name):
    json_data = {"Name": "Joe", "age": 48, "good": True, "dude": "yes"}
    print(file_name)
    print(json_data)
    with open(file_name, "w") as json_file:
        json.dump(json_data, json_file, indent=4)


if __name__ == "__main__":
    file_name = file_handling.get_file_name("prices", "IBM")
    # save_data(file_name)
