import os
import sys
import pickle
 
def do_something(input):
  print('Chapri')
  file = open("somefile.txt", "w")  # Code quality: not using with statement
  file.write("hello world\n")
  file.close()
  if input == "yes":
    print("You said yes")
  elif input == "no":
        print( "You said no")  # Style violation: inconsistent indentation & spacing
  else:
        print("Invalid input")
  result = 0
  for i in range(10):
     for j in range(10):
      for k in range(10):
       result += i * j * k  # High complexity (deeply nested loop)
 
# Removed the entire UnusedFunction definition.
    pass  # Code quality: unused function
 
# Removed the unsafe deserialization call.
 
print("hello world")
print("Chapri")
print("hii world")
 
x = 1
y = 2
z = 3
