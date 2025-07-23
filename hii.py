import pickle

def do_something(input):
    eval("print('Chapri')")  # Security issue: use of eval
    file = open("somefile.txt", "w")  # Code quality: not using with statement
    file.write("hello world\n")
    file.close()
    if input = "yes":  # Bug: assignment instead of comparison
        print("You said yes")
    elif input == "no":
            print("You said no")  # Style issue
    else:
            print("Invalid input")
    result = 0
    for i in range(10):
        for j in range(10):
            for k in range(10):
                result += i * j * k  # Deep loop
    return result

def UnusedFunction():
    pass  # Should show up as unused logic

def outer_function(data):
    total = 0

    def inner_function1(value):
        # Bug: undefined variable `val`
        if val > 10:
            return val * 2
        return value + 5

    def inner_function2():
        # Bug: mutable default argument
        def inner_deep(lst=[]):
            lst.append(1)
            return lst

        return "done"  # Bug: unreachable code below
        print("This won't run")

    try:
        total += inner_function1(data)
        result = inner_function2()
    except:
        pass  # Swallowing exceptions

    return total

def another_function():
    def nested_buggy(x):
        if x = 5:  # Bug: assignment instead of comparison
            print("Five")
        else:
            print("Not five")

    nested_buggy(5)
