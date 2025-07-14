"""This module provides an example script."""
# Removed this line
import pickle
 
def do_something(input_value):
  print('Chapri')
  with open("somefile.txt", "w", encoding='utf-8') as file:
  file.write("hello world\n")
  # Removed this line
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
    # Removed this function
 
# Removed this line
 
print("hello world")
print("Chapri")
print("hii world")
 
X = 1
Y = 2
Z = 3
