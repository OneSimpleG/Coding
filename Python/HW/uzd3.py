with open('rez2.txt','w')as f:
    pass
with open('temp.txt','r')as f:
    nepas = []
    pvzTemp = int(f.readline())
    temp = []
    kiek, dKiek, maxKiek, maxTemp = 0, 0, 0, 0
    for i in f.readline().split(' '):
        temp.append(int(i))
    for j in temp:
        if j > pvzTemp:
            dKiek+=1
        if not(j in nepas):
            nepas.append(j)
    nepas.sort()
    file = open('rez2.txt','a',encoding='utf-8')
    for i in nepas:
        kiek = temp.count(i)
        if kiek > maxKiek:
            maxKiek = kiek
            maxTemp = i
        file.write(f'{i} laipsniu temperatura buvo {kiek} d.\n')
    file.write(f'\n{dKiek} dienas temperatura buvo didesne uz {pvzTemp}\n')
    file.write(f'\nDaugiasiai, {maxKiek} dienas buvo {maxTemp} laipsniu')
file.close()
    