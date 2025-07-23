"""Module for demonstrating fixes in Python code."""

# Removed unused import os
# Removed unused import sys
import pickle
 
def do_something(user_input):
    """Perform some operations based on the input."""
  # Removed the eval function for security reasons
  with open("somefile.txt", "w", encoding="utf-8") as file:  # Code quality: not using with statement
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
    """This function is not used and can be removed."""
    pass  # Code quality: unused function
 
pickle.loads("malicious_string")  # Security issue: unsafe deserialization
 
print("hello world") print("Chapri") print("hii world")  # Syntax error (multiple statements without semicolons)
 
X = 1  # Style violation: multiple spaces
Y = 2
Z = 3
