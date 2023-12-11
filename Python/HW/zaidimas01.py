import random
m = 0
z = 0
zaid = 0
g = True
def valom():
    with open("01zaidRez.txt",'w') as f:
        pass
def rasom(txt):
    with open('01zaidRez.txt','a',encoding='utf-8') as f:
        f.write(f'{txt}\n')
valom()
while g:
    try:
        s = 1
        n = int(input('Iveskite sveika skaiciu: '))
        rasom(f'Vartotojas irase skaiciu: {n}')
        x = random.randint(1, n)
        rasom(f'Sugeneruotas skaicius: {x}')
        print('Atspekite koki skaiciu sugeneravo programa: ')
        while not(m == x):
            try:
                m = int(input())
                if 0<=m<=n:
                    if not(m == x):
                        if m > x:
                            rasom(f'{s} spejimu vartotojas ivede {m} - sugeneruotas skaicius mazesnis')
                            s+=1
                            print(f'sugenearuotas skaiciu yra mazesnis uz {m}. Atliksite {s} sprendima')
                        else:
                            rasom(f'{s} spejimu vartotojas ivede {m} - sugeneruotas skaicius didesnis')
                            s+=1
                            print(f'sugenearuotas skaiciu yra didesnis uz {m}. Atliksite {s} sprendima')
                    else:
                        rasom(f'{s} spejimu vartotojas atspejo sugeneruota skaiciu')
                        print(f'Atspejote sugeneruota skiaciu! sugeneruotas skaicius buvo {x}. Padaret per {s} spejimus. Buvo {z} neteisingu ivedimu')
                        k = input('Ar norite kartoti zaidima?(t/n)')
                        if k == 'n':
                            zaid += 1
                            rasom('I uzklausa "Ar norite kartoti zaidima?" vartotojas atsake "ne"')
                            rasom(f'Vartotojas zaide {zaid} kartu')
                            g =False
                        else:
                            zaid += 1
                            rasom('I uzklausa "Ar norite kartoti zaidima?" vartotojas atsake "taip"')
                            break
                else:
                    print('kartokite ivedima: ')
                    z+=1
                    continue
            except ValueError:
                print('kartokite ivedima: ')
                z+=1
                continue
    except ValueError:
        print('Blogai ivestas skaicius')
