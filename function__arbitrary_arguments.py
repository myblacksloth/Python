'''
~/Antonio_Maulucci@2019
'''

def myF(**args): # minimo 2 argomenti perche' il corpo della funziona elabora (teoricamente) un dizionario
    print(type(args))
    for k,v in args.items():
        print(f'{k}={v}')


def myF2(*arg):
    print(type(arg))
    for k in arg:
        print(k)

myF(capital='Roma', country='Italia') # -> dizionario
myF(capital='Roma', country='Italia', place='Mediterraneo')
print()
myF2([1,2,3,4,5], [6,7,8,9]) # -> tupla
myF2([1,2,3,4,5], [6,7,8,9], [10,11,12]) # -> tupla
''' out>
<class 'dict'>
capital=Roma
country=Italia
<class 'dict'>
capital=Roma
country=Italia
place=Mediterraneo

<class 'tuple'>
[1, 2, 3, 4, 5]
[6, 7, 8, 9]
<class 'tuple'>
[1, 2, 3, 4, 5]
[6, 7, 8, 9]
[10, 11, 12]
'''