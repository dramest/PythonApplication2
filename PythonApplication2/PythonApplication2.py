from random import *
inimesed = []
palgad= []
N=4
def sisesta_andmed(i,p):
    for n in range(N):
        inimene=input("Nimi: ")
        i.append(inimene)
        palk=randint(100,1000)
        p.append(palk)
    return i,p
def andmed_ekraanile(i,p):
    N=len(i)
    for n in range(N):
        print(i[n], "-", p[n])
def kustutamine(i,p):
    nimi=input("Sisesta nimi, keda vaja kustutada: ")
    n=i.count(nimi)
    abi_list[]
    if n > 0:
        for e in range(len(i)):
            if i[e]==nimi:
                t+=1
                abi_list.append(int(e))
                print(i[e], "+", p[e])
        j=int(input("Järjekordne number: "))
        i.pop(abi_list[j-1])
        p.pop(abi_list[j-1])
        andmed_ekraanile(i,p)

    return i,p
while 1:
    print("a-andmete siestamine\e-andmed ekraanile\k-kustutamine")
    valik=input()
    if valik.lower()=="a":
        inimesed, palgad = sisesta_andmed(inimesed, palgad)
    elif valik.lower()=="e":
        andmed_ekraanile(inimesed, palgad)
    elif valik.lower()=="k":
        inimesed, palgad = kustutamine(inimesed, palgad)
    else:
        break
