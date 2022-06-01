#elimar diferencia de listas elimina los valores de la lista a que se encuentren en la lista b

a=[9,4,6,43,6,7,5,7,3,63,4,7,2,5,7,1,2,2]

b=[2,4,6,7,2,9]
for e1 in b:
    
    while e1  in a:
        a.remove(e1)
print (a)


print([x for x in a if x not in b])
