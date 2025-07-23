"""
This module provides functionality to print messages and perform file operations.
"""


 
def do_something(input_value):
    """
    Perform actions based on the input value, write to a file, and calculate a result.
    """
  print('Chapri')
  with open("somefile.txt", "w", encoding='utf-8') as file:
  file.write("hello world\n")
  
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
    pass
 
# pickle.loads("malicious_string")  # Security issue: unsafe deserialization
 
print("hello world")
print("Chapri")
print("hii world")
 
X = 1
Y = 2
Z = 3