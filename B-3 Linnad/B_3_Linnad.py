from module import*

linnad=[]
elanikkond=[]

n=int(input("Sisestage linnade arv: "))
for j in range(n):
    linn=input("Sisesta linna nimi: ")
    elanik=int(input("Sisesta elaniku arv: "))
    linnad.append(linn)
    elanikkond.append(elanik)
print(linnad,elanikkond)
while True:
        menu=int(input("1 Uurige linna nime sisestades, kui palju elanikke selles on\n2 Kuva tähestikulises järjekorras linnade nimekiri ja elanike arv\n3 Leidke linna elanike arv, sisestades selle nime\n4 Leia linnad, kus on vähem kui n elanikku\n5 Oma variant(max/min)\n"))
        if menu==1:
            elanike_arv(elanikkond,linnad)
        elif menu==2:
            tähestik(elanikkond,linnad)
        elif menu==3:
            nimi_populatsioon(elanikkond,linnad)
        elif menu==4:
            vähem(elanikkond,linnad)
        elif menu==5:
            oma_variant(elanikkond,linnad)
        else:
            print("Error")