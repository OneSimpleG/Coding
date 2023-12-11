#Duatas sarasas m = [5,8,8,5,7,4,1,1,'Labas',5,8,-7,-7,'Labas']
#Atspausdinti kiek kiekvieno elemento yra
#Pvz:   5 yra 3
#       8 yra 7
#       7 yra 1
#       4 yra 1
#       1 yra 2
#       labas yra 2
#       -7 yra 2
#Negalima naudoti dict set
m = [5,8,8,5,7,4,1,1,'Labas',5,8,-7,-7,'Labas']
nepas = []
for i in m:
    if not(i in nepas):
        nepas.append(i)

for i in nepas:
    print(f'{i} yra {m.count(i)}')