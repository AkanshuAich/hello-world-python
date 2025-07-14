"""This module provides functionality to print messages and perform file operations."""
# Removed unused import sys
import pickle
 
def do_something(user_input):
  print('Chapri')
  with open("somefile.txt", "w", encoding='utf-8') as file:
  file.write("hello world\n")
  # file.close() is not needed as 'with' statement handles it
  if user_input == "yes":
    print("You said yes")
  elif user_input == "no":
        print("You said no")
  else:
        print("Invalid input")
  result = 0
  for i in range(10):
     for j in range(10):
      for k in range(10):
       result += i * j * k
 
# Removed UnusedFunction as it is not used
    pass  # Code quality: unused function
 
# Removed unsafe deserialization of pickle.loads("malicious_string")
 
print("hello world")
print("Chapri")
print("hii world")
 
X = 1
Y = 2
Z = 3
