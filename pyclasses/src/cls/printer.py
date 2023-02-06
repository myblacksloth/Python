
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

class laserPlotter(plotter): # e' una sottoclasse di plotter
        def __init__(self, custom=None):
                super().__init__(custom)
                self.laserType = True
                if self.tipo != "laser":
                        self.tipo = self.tipo+"__laserType"

        def isLaser(self):
                # if self.laserType:return True
                # else: return False
                return self.laserType
