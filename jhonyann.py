#John y Ann se registran en Codewars
'''
En el día, n el número de katas realizados por John debe ser n menos 
el número de katas realizados por Ann en el día t, 
t siendo igual al número de katas realizados por el mismo John en el día 
n - 1

'''
n=11
nlistj=[]
for i in range(0,n):
    t= i-1
    
    nlistj.append(i-t)
print(nlistj)