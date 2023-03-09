
from enum import Enum

# librerie [*1]
from src.algos.firstAlgo import FirstAlgo
from src.algos.secondAlgo import SecondAlgo


class ManyChoices(Enum):
    # se non vengono importate le librerie realtive [*1]
    #   viene rilevato un errore
    # quindi questo e' il metodo in cui viene selezionata la configurazione
    A = FirstAlgo
    B = SecondAlgo


ALGO = ManyChoices.A


