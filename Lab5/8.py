import re
def split_string_at_uppercase(string):
    return re.findall('[A-Z][^A-Z]*', string)