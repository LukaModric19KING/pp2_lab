def globFunc():
  global x
  x = "Global"

globFunc()

print("That function is " + x)