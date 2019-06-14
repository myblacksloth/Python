class mysum:

    a = 0

    def __init__(self, a):
        self.a = a
    
    # override the python sum (+)
    # obj + b
    def __add__(self, b):
        return (self.a+b)*2

    # b + obj
    def __radd__(self, b):
        return (self.a + b)