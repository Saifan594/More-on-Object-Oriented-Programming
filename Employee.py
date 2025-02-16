print("\033c")

class Employee():
    def __init__(self):
        print("Employee created")
    
    def __del__(self):
        print("Destructor called")

def createObj():
    print("Making an object")
    print()
    
    obj = Employee()
    print()
    
    print("Function end...")
    print()
    
    return obj

print("Calling createObj() function")

obj = createObj()

print("Program end")
print()