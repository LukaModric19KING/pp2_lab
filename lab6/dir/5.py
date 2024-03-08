def write_list_to_file(filename, lst):
    with open(filename, "w") as file:
        for item in lst:
            file.write(str(item) + "\n")

# Sample usage
filename = "output.txt"
my_list = [1, 2, 3, 4, 5]
write_list_to_file(filename, my_list)
