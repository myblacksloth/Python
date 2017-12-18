#compatible with Python 2.7

def __sum__(x, y):
	return x+y


def __mult__(x, y):
	return x*y

def __pot__(m, e):
	for i in range (0, e-1):
		m += m
	return m



class newclass:

	i = 0
	j = 0

	def __init__(self): #dovrebbe essere il costruttore della classe
		i = 0
		j = 0	

	

	def setter(self, i, j):
		self.i = i
		self.j = j

	def __rest__(self, i, j):
		return (self.i%self.j)

	def __toString__(self):
		print "i = ", self.i, " j = ", self.j