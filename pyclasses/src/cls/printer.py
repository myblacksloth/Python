
class printer:

        printed = 0

        def __init__(self):
                self.printed = 0

        def printed_pages(self):
                return self.printed
        
        def printTxt(self, txt):
                print(txt)
                self.printed += 1

class plotter:
        def __init__(self, custom=None):
                self.printed=0
                self.tipo = custom['tipo']
        
        def getType(self):
                return self.tipo