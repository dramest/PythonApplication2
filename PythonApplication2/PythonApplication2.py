from random import *

def sisesta_andmed(i,p):
    global N
    N=4
    for n in range(N):
        inimene=input("Nimi:")
        i.append(inimene)
        palk=randint(100,10000)
        p.append(palk)
    return i,p

def andmed_ekranile(i,p):
    N=len(i)
    for n in range(N):
        print(i[n],"-",p[n])

def kustutamine(i,p): #Kustuta inimese nimi ja palga
    nimi=input("Sisesta nimi, keda vaja kustutada:")
    n=i.count(nimi)
    abi_list=[]
    if n>0:
        t=0
        for e in range(len(i)):
            if i[e]==nimi:
                t+=1
                abi_list.append(int(e)) #indeksite nimekiri
                print(t,". ",i[e],"-",p[e])
        j=int(input("Järjekordne number:"))
        i.pop(abi_list[j-1])
        p.pop(abi_list[j-1])
        andmed_ekranile(i,p)
    return i,p

def suurim_palk(i,p):
    suurim=max(p)
    #count() for abi_list p.index()->i.index() andmed_ekranile(abi_list)
def sorteerimine(i,p,v):
    N=len(p)
    if v==1:
        for n in range(0,N):
            for m in range(n,N):
                if p[n]<p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi
    else:
        for n in range(0,N):
            for m in range(n,N):
                if  p[n]>p[m]:#< - >
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi
    andmed_ekranile(i,p)
    return i,p
def sort_nimi_jargi(p,i,v):
    N=len(p)
    if v==1:
        for n in range(0,N):
            for m in range(n,N):
                if p[n]<p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi
    else:
        for n in range(0,N):
            for m in range(n,N):
                if  p[n]>p[m]:#< - >
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi
    andmed_ekranile(i,p)
    return i,p
def vordsed_palgad(i,p):
    N=len(p)
    dublikatid=[x for x in p if p.count(x)>1 ]
    dublikatid=list(set(dublikatid))
    print(dublikatid) #[2000,122]
    for palk in dublikatid: #2000, n=3
        n=p.count(palk)
        k=-1 #-----
        for j in range(n):            
            k=p.index(palk,k+1)#-----
            nimi=i[k]
            print(palk,"saab kätte",nimi)
def keskmine(i,p):
    summa=0
    t=True
    for palk in p:
        summa+=palk
    summa/=len(p)
    print("Keskmine palk: ",summa)
    for palk in p:
        if palk==summa:
            n=p.index(palk)
            print("Saab kätte",i[n])
        else:
            t=False
        if t==False:   print("Sellised inimesed puudubad")
inimesed=["A","B","C"]
palgad=[3000,2000,1000]
keskmine(inimesed, palgad) 

while 1:
    print("a-sisesta\ne-ekaranile\nk-kustuta\nmax-kellel on suurim palk\ns-sort")
    valik=input()
    if valik.lower()=="a":
        inimesed,palgad=sisesta_andmed(inimesed,palgad)
    elif valik.lower()=="e":
        andmed_ekranile(inimesed,palgad)
    elif valik.lower()=="k":
        inimesed,palgad=kustutamine(inimesed,palgad)
    elif valik.lower()=="max":
        suurim_palk(inimesed,palgad)
    elif valik.lower()=="s":
        inimesed,palgad=sorteerimine(inimesed,palgad,int(input("1-kahaneb, 2-kasvab ")))
    elif valik.lower()=="d":
        vordsed_palgad(inimesed,palgad)
    else:
        break

