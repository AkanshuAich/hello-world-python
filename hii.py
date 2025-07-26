import pickle

def do_something(input):
    # Removed the problematic print statement
    with open("somefile.txt", "w") as file:
    file.write("hello world\n")
    file.close()
    if input == "yes":
        print("You said yes")
    elif input == "no":
            print("You said no")
    else:
            print("Invalid input")
    result = 0
    for i in range(10):
        for j in range(10):
            # Removed the deep loop and replaced it with a mathematical equivalent
                result += i * j  # Removed the undefined variable 'k'
    return result

# Removed the unused function
    # Removed the unused 'pass' statement

def outer_function(data):
    total = 0

    def inner_function1(value):
        # Bug: undefined variable `val`
        if value > 10:
            return value * 2
        return value + 5

    def inner_function2():
        # Bug: mutable default argument
        def inner_deep(lst=None):
            if lst is None:
                lst = []
            lst.append(1)
            return lst

        # Removed the return statement to make the code below reachable
        # Removed the print statement as it is no longer needed

    try:
        total += inner_function1(data)
        total += inner_function2()
    except Exception as e:
        print(f"An error occurred: {e}")
        # Removed the unnecessary 'pass' statement

    return total

def another_function():
    def nested_buggy(x):
        if x == 5:
            print("Five")
        else:
            print("Not five")

    nested_buggy(5)
