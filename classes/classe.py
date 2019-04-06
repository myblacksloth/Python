# python 3

def somma(x, y):
    return x + y

class classe:

    @staticmethod
    def getHello(name):
        return "Hello, " + name + "!"

    def getNome(self, nome):
        return nome


class animale:

    @staticmethod
    def getVerso(verso):
        return verso
    
    # un metodo che non prende 'self' come paramentro viene automaticamente
    #   riconosciuto come metodo statico
    def getZampe():
        return 4

class persona:

    nome = ""
    cognome = ""
    eta = -1

    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    def getName(self):
        return self.nome

    def getData(self):
        # restituisce una tupla con i dati della persona
        return self.nome, self.cognome, self.eta