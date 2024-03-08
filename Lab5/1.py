import re
def match_zero_or_more_b():
    with open("row.txt", "r") as file:
        text = file.read()
        pattern = r'ab*'
        matches = re.findall(pattern, text)
        print(matches)