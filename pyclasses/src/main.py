
from src.cls.printer import printer, plotter, laserPlotter
from src.cls.dispatcher import Dispatcher, Postman

def main():

        pr = printer() # nuovo oggetto
        print("l'oggetto pr e' di tipo printer? {}".format(isinstance(pr, printer)))
        pr.printTxt("hello")

        cdata = {}
        cdata['tipo']='plotter'
        
        pl = plotter(custom=cdata)
        print("il tipo di pl e' {}".format(pl.getType()))

        lpl = laserPlotter(custom=cdata)
        print("il tipo di lpl e' {}".format(lpl.getType()))

        d = Dispatcher()
        d.send('ciao')
        d.send('come')
        d.send('stai')
        d.run()
        p = Postman()
        p.send('ciao', Dispatcher())
        print(p.check(Dispatcher())) # []


if __name__ == "__main__":
        main()

