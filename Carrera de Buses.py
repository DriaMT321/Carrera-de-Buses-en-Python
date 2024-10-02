def buses(n1,n2):
    print(115*"-")
    print( (n1*" ") + "__________________"    +((100-n1)*" " )+"|" )
    print( (n1*" ") + "|__|__|__|__|__|__|_"  +((97-n1)*" " )+" |" )
    print( (n1*" ") + "|        74         |" +((96-n1)*" " )+" |" )
    print( (n1*" ") + "|---O-----------O---|" +((96-n1)*" " )+" |" )
    print(115*"-")
    print( (n2*" ") + "__________________"    +((100-n2)*" " )+"|" )
    print( (n2*" ") + "|__|__|__|__|__|__|_"  +((97-n2)*" " )+" |" )
    print( (n2*" ") + "|        72         |" +((96-n2)*" " )+" |" )
    print( (n2*" ") + "|---O-----------O---|" +((96-n2)*" " )+" |" )
    print(115*"-")
    return 'carrera de MICROS'

import time
import os
from random import randint

a = 0
b = 0
print("CARRERA DE MICROS!!!!")
print("LA 74 VS LA 72")
time.sleep(3)
os.system("cls")

while (a<97) and (b<97):
    c = randint(1,2)
    if c == 1:
        a +=1
    if c == 2:
        b +=1
    os.system("cls")
    print(buses(a,b))
    time.sleep(0.005)

if a == 97:
    gano = "74"
if b == 97:
    gano = "72"

print("GANO LA "+ gano)