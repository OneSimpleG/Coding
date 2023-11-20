a=int(input('Iveskite intervalo pradzia: '))
b=int(input('Iveskite intervalo pabaiga: '))
m=int(input('Kuria savaites diena prasideda menuo: '))
n=0
for i in range(1,32):
    if m==8:
        m=1
    if a<=i<=b:
        print(f'{i}-oji diena yra: {m}')
    m+=1