m = int(input('Iveskite metus: '))
if m < 1896:
    print('metai turi buti didesni uz 1896')
elif m%4==0:
    x=((m-1896)//4)+1
    print(f'Metu {m} eile yra {x}')
else:
    print('metai ne olimpiniai')