"""
This module provides an example script with various issues to be fixed.
"""
# import sys
import pickle
 
def do_something(user_input):
    """
    Perform operations based on the user input.
    """
  print('Chapri')  # Removed eval to address security issue
  with open("somefile.txt", "w", encoding="utf-8") as file:  # Specified encoding and used with statement
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
    pass
 
# # pickle.loads("malicious_string")  # Security issue: unsafe deserialization
 
print("hello world")
print("Chapri")
print("hii world")  # Removed comment about syntax error as it is not applicable
 
X = 1
Y = 2
Z = 3
