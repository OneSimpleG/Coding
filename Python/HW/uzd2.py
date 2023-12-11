with open('duom2.txt','r') as f:
    mokKiek = len(f.readlines())
with open('paz.txt','w') as f:
    pass
with open('duom2.txt','r',encoding='utf-8') as f:
    for i in range(0,mokKiek):
        totalSum = 0
        HTMLSum = 0
        PYnum = 0
        mokInfo = f.readline().split(' ')
        dienPos = mokInfo.pop(0)
        for j in mokInfo:
            j = int(j)
            if j > 0:
                HTMLSum+=j
            elif j < 0:
                PYnum+=1
            j = abs(j)
            totalSum+=j
        totalAvg = round((totalSum/len(mokInfo)),2)
        HTMLAvg = round((HTMLSum/(len(mokInfo)-PYnum)),2)
        file = open('paz.txt','a')
        file.write(f'Mokinys Nr. {dienPos} vidurkis HTML ir Python yra {totalAvg}. Tik HTML vidurkis {HTMLAvg}\n')
file.close()