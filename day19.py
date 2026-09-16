#statements
print('HI')
print('Welcome to the calculator application')
print('USE FUNCTION TO PERFORM CALCULATIONS')
#Function to perform addition
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
#classes
class calculator:
    def __init__(self):
        self.result = 0

    def add(self, x, y):
        self.result = x + y
        return self.result

    def sub(self, x, y):
        self.result = x - y
        return self.result

    def mul(self, x, y):
        self.result = x * y
        return self.result
    __all__ = ['add']