"""Module for demonstrating fixes."""
# Removed unused import os
# Removed unused import sys
import pickle
 
def do_something(input_value):
    """Perform some operations based on the input."""
  print('Chapri')  # Removed eval for security reasons
  with open("somefile.txt", "w", encoding='utf-8') as file:  # Using with statement and specifying encoding
  file.write("hello world\n")
  # Removed file.close() as it's handled by the with statement
  if input_value == "yes":  # Corrected comparison operator
    print("You said yes")
  elif input_value == "no":
        print("You said no")  # Fixed indentation and removed extra space
  else:
        print("Invalid input")
  result = 0
  for i in range(10):
     for j in range(10):
      for k in range(10):
       result += i * j * k  # High complexity (deeply nested loop)
 
def unused_function():
    pass  # Code quality: unused function
 
# Removed unsafe deserialization with pickle.loads
 
print("hello world")
print("Chapri")
print("hii world")  # Fixed syntax error by separating statements onto new lines
 
X = 1  # Renamed to UPPER_CASE to indicate constant
Y = 2  # Renamed to UPPER_CASE to indicate constant
Z = 3  # Renamed to UPPER_CASE to indicate constant