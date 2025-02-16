print("\033c")

class IOString():
    def __init__(self):
        self.str = ""
    
    def getString(self):
        self.str = input("Enter a string: ")
    
    def printString(self):
        print(f"Result is: {self.str.upper()}")

string1 = IOString()

string1.getString()
string1.printString()