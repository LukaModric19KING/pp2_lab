import re
def match_a_followed_by_anything_ending_b():
    with open("row.txt", "r") as file:
        text = file.read()
        pattern = r'a.*?b$'
        matches = re.findall(pattern, text)
        print(matches)
