import os

def check_path_access(path):
    print("Path:", path)
    print("Exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))

# Sample usage
path = "/path/to/file_or_directory"
check_path_access(path)
