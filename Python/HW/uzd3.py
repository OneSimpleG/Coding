n = int(input('kiek septynetu turi paskutinis skaicius: '))
d=1
suma=0
for i in range(1,n+1):
    if i<n:
        txt = ' + '
    else:
        txt = ' = '
    print(7*d,end=txt)
    d=d+(10**i)
    suma=suma+(7*d)
print(suma)