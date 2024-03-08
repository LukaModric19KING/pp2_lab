import re
def find_uppercase_followed_by_lowercase():
    with open("row.txt", "r") as file:
        text = file.read()
        pattern = r'[A-Z][a-z]+'
        matches = re.findall(pattern, text)
        print(matches)