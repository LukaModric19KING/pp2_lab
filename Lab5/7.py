def snake_case_to_camel_case(snake_case_str):
    words = snake_case_str.split('_')
    return ''.join(word.capitalize() for word in words)

