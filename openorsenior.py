data=[(45, 12),(55,21),(19, -2),(104, 20)]
lista=[]
valor=""
for edad, desventaja in data:
    if edad>=55 and desventaja>=7:
        lista.append("Senior")
    else:
        lista.append("Open")
print (lista)

def openOrSenior(data):
  return ["Senior" if edad >= 55 and desventaja >= 8 else "Open" for (edad, desventaja) in data]

print(openOrSenior(data))