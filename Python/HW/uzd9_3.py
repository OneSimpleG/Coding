x = int(input('Iveskite keturzenkli skaiciu: '))
l = []
nl= []
if x < 1000 or x > 9999:
    print('Netinkamas skaicius')

def sn(x):
    n=str(x)
    n=''.join(sorted(n, reverse=True))
    n=int(n)
    return n
xs1=sn(x)//1000
xs2=sn(x)//100%10
xs3=sn(x)//10%10
xs4=sn(x)%10
if xs1%2==0 or xs1==0:
    l.append(int(xs1))
else:
    nl.append(int(xs1))
if xs2%2==0 or xs2==0:
    l.append(int(xs2))
else:
    nl.append(int(xs2))
if xs3%2==0 or xs3==0:
    l.append(int(xs3))
else:
    nl.append(int(xs3))
if xs4%2==0 or xs4==0:
    l.append(int(xs4))
else:
    nl.append(int(xs4))
mlist=(l+nl)
nlist=[str(ci) for ci in mlist]
strlist=''.join(nlist)
flist=int(strlist)
print(flist)