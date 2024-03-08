import re
def match_two_to_three_b():
    with open("row.txt", "r") as file:
        text = file.read()
        pattern = r'ab{2,3}'
        matches = re.findall(pattern, text)
        print(matches)