import random
def valom():
    with open('02zaidRez.txt','w') as f:
        pass
valom()
def rasom(txt):
    with open('02zaidRez.txt','a',encoding='utf-8') as f:
        f.write(f'{txt}\n')
zaid1 = input('Iveskite pirmo zaidejo varda ')
zaid2 = input('Iveskite antro zaidejo varda ')
rasom(f'zaideju vardai: {zaid1} ir {zaid2}')
zaidSar = [zaid1,zaid2]
 
x = random.choice(zaidSar)
kartu = 0
game = True
def eile():
    global x
    if x == zaidSar[0]:
        x = zaidSar[1]
    else:
        x = zaidSar[0]
    return x
while game:
    try:
        lazd = int(input('Iveskite lazdeliu skaiciu: '))
        rasom(f'Lazdeliu pasirinktas skaicius yra {lazd}')
        print(f'Zaidima pradeda {x}')
        rasom(f'zaidima pradeda {x}')
        while lazd>0:
            try:
                lazdMinus = int(input(f'Kiek lazdeliu paimsit? liko {lazd} '))
                if 0<lazdMinus<=3 and 0<lazdMinus<=lazd:
                    lazd -= lazdMinus
                    rasom(f'{x} paima {lazdMinus} lazdeliu. Liko {lazd}')
                else:
                    continue
            except ValueError:
                print ('netaip ivestas skaicius')
                continue
            if lazd>0:print(f'{eile()} eile')
        if lazd<=0:
            print(f'laimejo {eile()}')
            rasom(f'Zaidima laimejo {x}')
            test = input('Ar norite dar?(t/n)').lower()
            if test == 't':
                kartu+=1
                rasom('I uzklausa "Ar norite dar?" pasirinko "Taip"')
                continue
            else:
                kartu+=1
                rasom('I uzklausa "Ar norite dar?" pasirinko "Ne"')
                game=False
    except ValueError:
        print ('netaip ivestas skaicius')
rasom(f'Zaidima zaide {kartu} karta(us)')