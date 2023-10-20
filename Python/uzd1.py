k = int(input('Iveskite lentos gyli: '))
n = int(input('Iveskite vinies ilgi: '))
for i in range(1,k):
    k-=n
    print(f'Tuk! {i}')
    if k==0:
        break
print('Vinis ikalta')