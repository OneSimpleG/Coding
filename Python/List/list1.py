#Petriuko, Antano, Stasio.... pazymiai
# Ivedamas pazymiu kiekis ir suvedami pazymiai. rasti vidurki
#sukurti sarasa mamai (tik teigiami) 4 ir didesi ir apskaiciuoti vidurki
#sukurti sarasa teciui (tik teigiami) 6 ir didesi ir apskaiciuoti vidurki
MAMA = 4
TETIS = 6
#------Gaunamas pazimiu kiekis-----------------------------------------
def kiekis(vardas):
    kiek  = int(input(f'Kiek {vardas} turi pazymiu? '))
    return kiek
#------Gaunamas pazimiu saras------------------------------------------
def Ivedimas(kiek, vardas):
    p = []
    i = 0
    while i < kiek:
        paz = int(input(f'Įveskite {vardas} {i+1}-aji pažymį...'))
        if 1<=paz<=10:
            p.append(paz)
            i += 1
        else:
            print(f'Pazymys {paz} neegzistuoja. Kartokite ivedima ')
    return p
#------Skaicuojamas vidurkis-------------------------------------------
def vidurkis(p):
    if len(p) > 0:
        return (sum(p) / len(p))
    else:
        return 0
#------Kuriamas tevu pazimiu sarasas-----------------------------------
def tevams(p, kriterijus):
    pTev = []
    for i in p:
        if i >= kriterijus:
            pTev.append(i)
    return pTev
#------Isvedama informacija--------------------------------------------
def isvedimas(vardas):
    paz = Ivedimas(kiekis(vardas), vardas)
    pazMama = tevams(paz, MAMA)
    pazTetis = tevams(paz, TETIS)
    print(f'{vardas} pazymiai {paz}. Vidurkis {vidurkis(paz)}')
    print(f'{vardas} mamos pazymiai {pazMama}. Vidurkis {vidurkis(pazMama)}')
    print(f'{vardas} tetcio pazymiai {pazTetis}. Vidurkis {vidurkis(pazTetis)}')

klase = ['Petras','Antanas','Stasys','Rimas','Jonas','PetrasDidysis']
for i in klase:
    isvedimas(i)
