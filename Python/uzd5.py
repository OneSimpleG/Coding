m=int(input('Iveskite laimingojo bileto intervalo pradzia: '))
n=int(input('Iveskite laimingojo bileto intervalo pabaiga: '))
suma=0
for i in range(m,n):
    s1=i//1000
    s2=i%1000
    if s1==s2:
        suma+=1
print(f'Isviso laimingu biletu yra: {suma}')