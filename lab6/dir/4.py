def count_lines(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        return len(lines)

# Sample usage
filename = "example.txt"
print("Number of lines in", filename, ":", count_lines(filename))
