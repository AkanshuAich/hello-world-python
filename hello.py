"""Module for demonstrating code fixes."""

# import os  # Unused import
# import sys  # Unused import
import pickle
 
def do_something(input_value):
    """Perform actions based on the given input."""
  print('Chapri')  # Removed eval for security reasons
  with open("somefile.txt", "w", encoding='utf-8') as file:
  file.write("hello world\n")
  # file.close()  # No longer needed due to 'with' statement
  if input_value == "yes":
    print("You said yes")
  elif input_value == "no":
        print("You said no")
  else:
        print("Invalid input")
  result = 0
  for i in range(10):
     for j in range(10):
      for k in range(10):
       result += i * j * k
 
def unused_function():
    """An unused function."""
    pass
 
# pickle.loads("malicious_string")  # Commented out due to security issue: unsafe deserialization
 
print("hello world") print("Chapri") print("hii world")  # Syntax error (multiple statements without semicolons)
 
X = 1
Y = 2
Z = 3