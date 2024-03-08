import time
import math

def square_root_after_milliseconds(number, milliseconds):
    time.sleep(milliseconds / 1000)
    result = math.sqrt(number)
    return result

# Sample usage
number = 25100
milliseconds = 2123
print("Square root of", number, "after", milliseconds, "milliseconds is", square_root_after_milliseconds(number, milliseconds))