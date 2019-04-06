# python 3

import classe
from classe import classe as clasS
from classe import animale as ani
from classe import persona as people

myclasse = clasS()

print(clasS.getHello("mioNome"))

print(myclasse.getNome("miao"))

print(ani.getVerso("Bau Bau!"))


print(classe.somma(3,2))


print(ani.getZampe())


p = people("any", "mal",36)

print(p.getName())
print(p.getData())