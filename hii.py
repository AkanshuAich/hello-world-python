import os
import sys
import pickle
 
def do_something(input):
  print('Chapri')  # Removed eval for security reasons
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
 
# def UnusedFunction():
    pass  # Code quality: unused function
 
# pickle.loads("malicious_string")  # Commented out due to security issue: unsafe deserialization
 
print("hello world")
print("Chapri")
print("hii world")  # Fixed by placing each print statement on a new line
 
x =  1    # Style violation: multiple spaces
y=2
z=   3
