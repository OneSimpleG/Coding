with open('duom.txt','r',encoding='utf-8') as f:
    skmas = f.readline().split(' ')
pos = 0
with open('rez.txt','w',encoding='utf-8') as f:
    pass
for i in range(1,len(skmas)):
    sk1 = int(skmas.pop(0))
    sk2 = int(skmas.pop(0))
    if sk1 > sk2:
        text = 'Pirmas skaicius sunaikina antra skaiciu'
        plius = sk1 - sk2
        sk1+=plius
        skmas.insert(0,sk1)
    elif sk2 > sk1:
        text = 'Antras skaicius sunaikina pirma skaiciu'
        plius = sk2 - sk1
        sk2+=plius
        skmas.insert(0,sk2)
    elif sk1 == sk2:
        text = 'Lygiosios. Skaiciai susijungia'
        plius = sk1 + sk2
        skmas.insert(0,plius)
    with open('rez.txt','a',encoding='utf-8') as f:
        f.write(f'{i} kova. {text}\n')
        f.write(f'Rezultatas {skmas}\n')