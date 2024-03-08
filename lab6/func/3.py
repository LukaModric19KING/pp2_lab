def is_palindrome(string):
    return string == string[::-1]

# Sample usage
string = "radar"
print("Is the string a palindrome?", is_palindrome(string))