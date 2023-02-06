
from src.cls.printer import printer, plotter

def main():

        pr = printer() # nuovo oggetto
        print("l'oggetto pr e' di tipo printer? {}".format(isinstance(pr, printer)))

        pr.printTxt("hello")

        cdata = {}
        cdata['tipo']='plotter'
        pl = plotter(custom=cdata)
        print("il tipo di pl e' {}".format(pl.getType()))


if __name__ == "__main__":
        main()

