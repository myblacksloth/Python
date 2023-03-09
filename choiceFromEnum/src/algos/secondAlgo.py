
from src.algos.algo import Algo

class SecondAlgo(Algo): # sottoclasse
    def __init__(self, id:int=None):
        Algo.__init__(self, id=id)
