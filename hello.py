"""This module provides functionality to print messages and perform file operations."""
# import sys
import pickle
 
def do_something(user_input):
    """Perform actions based on the user input."""
  print('Chapri')  # Removed eval to address security issue
  with open("somefile.txt", "w", encoding="utf-8") as file:  # Using with statement and specifying encoding
        file.write("hello world\n")
  file.write("hello world\n")
  file.close()
  if input == "yes":  # Potential bug: wrong comparison operator
    print("You said yes")
  elif input == "no":
        print("You said no")  # Style violation: inconsistent indentation & spacing
  else:
        print("Invalid input")
  result = 0
  for i in range(10):
     for j in range(10):
      for k in range(10):
       result += i * j * k  # High complexity (deeply nested loop)
 
def unused_function():
    pass  # Code quality: unused function
 
# pickle.loads("malicious_string")  # Security issue: unsafe deserialization
 
print("hello world")
print("Chapri")
print("hii world")  # Syntax error (multiple statements without semicolons)
 
X = 1  # Renamed to UPPER_CASE to indicate a constant
Y = 2  # Renamed to UPPER_CASE to indicate a constant
Z = 3  # Renamed to UPPER_CASE to indicate a constant
