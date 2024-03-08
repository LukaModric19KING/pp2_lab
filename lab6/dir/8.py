import os

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print("File deleted successfully.")
        else:
            print("No write access to the file.")
    else:
        print("File does not exist.")

# Sample usage
file_path = "/path/to/file"
delete_file(file_path)
