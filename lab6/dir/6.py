import string

def generate_files():
    for letter in string.ascii_uppercase:
        with open(letter + ".txt", "w") as file:
            pass

# Sample usage
generate_files()
