# import classes.mysum
# from classes.mysum import mysum

'''
python 3
'''
import sys
sys.path.insert(0, './classes/')
import mysum


'''
python 3
'''
# mysum e' il modulo
# mysum.mysum e' la classe
s = mysum.mysum(3)

print(3+2) #> 5

print(s+2) #> 10

print(2+s) #> 5
