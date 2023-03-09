
from datetime import datetime
from src.util import conf

class Envi:
    def __init__(self):
        self.id = datetime.now()
        self.algo = conf.ALGO
        self.algoValue = conf.ALGO.value(id=10) # creo l'oggetto

    def run(self):
        print(f"current algo is {self.algo}")
        print(f"current algo is {self.algoValue}")
