import os

def test_path(path):
    if os.path.exists(path):
        print("Path exists.")
        print("Filename:", os.path.basename(path))
        print("Directory:", os.path.dirname(path))
    else:
        print("Path does not exist.")

# Sample usage
path = "/path/to/file_or_directory"
test_path(path)
