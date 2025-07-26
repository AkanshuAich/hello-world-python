import os
import sys
import pickle
# import hii  # Importing the hii module

def main():
    user_input = "yes"
    hii.do_something(user_input)

    print("Calling outer_function from hii:")
    result = hii.outer_function(15)  # Cross-module call
    print(f"Result from outer_function: {result}")

    print("Calling another_function from hii:")
    hii.another_function()  # Cross-module call

    # unused = hii.UnusedFunction()  # Should be detected as unused even if called like this

    # Security issue still here
    # eval("print('Eval used in hello.py')")

    # Deserialization issue
    # pickle.loads("malicious_string")

    # Syntax error example (intended)
    print("hello from hello.py")
print("this will cause a syntax error")

if __name__ == "__main__":
    main()
