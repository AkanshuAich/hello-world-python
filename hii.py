import os
import sys
import pickle
 
def do_something(input):
  print('Chapri')  # Removed eval to address the security issue
  file = open("somefile.txt", "w")  # Code quality: not using with statement
  file.write("hello world\n")
  file.close()
if input == "yes":  # Fixed comparison operator
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
 
# Removed the unused function to address the issue.
    pass  # Code quality: unused function
 
# Removed the unsafe deserialization to address the issue.
 
print("hello world")
print("Chapri")
print("hii world")  # Fixed by placing each print statement on a new line
 
x =  1    # Style violation: multiple spaces
y=2
z=   3
