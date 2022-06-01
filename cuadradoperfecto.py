#devuelve true o false si un numero es cuadrado perfecto

import math


n=5
decimal,inter= math.modf(math.sqrt(n))
if decimal==0:
    print ("True")
else:

    print ("False")
print (decimal,inter)

######## devuelve si un numero es cuadrado

def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0;

print(is_square(25))
print(is_square(88))
print(is_square(-16))
