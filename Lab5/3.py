import re
def find_lowercase_with_underscore():
    with open("row.txt", "r") as file:
        text = file.read()
        pattern = r'[a-z]+_[a-z]+'
        matches = re.findall(pattern, text)
        print(matches)
