"""Module docstring: This module does something."""
# Removed unused import sys
import pickle
 
def do_something(input_value):
  print('Chapri')  # Removed eval for security reasons
  with open("somefile.txt", "w", encoding='utf-8') as file:  # Using with statement and specifying encoding
  file.write("hello world\n")
  # Removed file.close() as it's handled by the with statement
  if input_value == "yes":  # Corrected variable name
    print("You said yes")
  elif input_value == "no":
        print("You said no")  # Corrected spacing
  else:
        print("Invalid input")
  result = 0
  for i in range(10):
     for j in range(10):
      for k in range(10):
       result += i * j * k  # High complexity (deeply nested loop)
 
def unused_function():
    pass
 
# Removed unsafe deserialization with pickle.loads
 
print("hello world") print("Chapri") print("hii world")  # Syntax error (multiple statements without semicolons)
 
X = 1
Y = 2
Z = 3
