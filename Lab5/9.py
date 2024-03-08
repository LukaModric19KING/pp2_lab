import re
def insert_spaces_between_capital_words(string):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', string)