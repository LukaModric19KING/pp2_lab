import re
def replace_space_comma_dot_with_colon():
    with open("row.txt", "r") as file:
        text = file.read()
        pattern = r'[ ,.]'
        replaced_text = re.sub(pattern, ':', text)
        print(replaced_text)