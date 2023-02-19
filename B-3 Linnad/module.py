def elanike_arv(e:list,l:list):
    """Otsib nime järgi välja elanike arvu linnas"""
    linn=input("Sisestage linna nimi, mille elanike arvu soovite teada:")
    while linn not in l:
        linn=input("Palun kirjuta õige linna nimi\n")
    print(f"Linnas {linn} on ",e[l.index(linn)]," elanikud\n")


def tähestik(e:list,l:list):
    """sorteerib linnade nimekirja, võtab rahvastikuandmed ja annab need vastavatesse indeksitesse"""
    l_copy=l.copy()
    l_copy.sort()
    sorted_elanikud=[]
    for element in l_copy: #võtab loendist elemendi
        temp_var=l.index(element) #võtab loendis oleva elemendi indeksi ja määrab selle ajutisele muutujale
        sorted_elanikud.append(e[temp_var]) #asendab elemendi indeksis
    print("Linnad tähestikulises järjekorras ja nende elanikkond.")
    print(l_copy)
    print(sorted_elanikud)
    print()


def nimi_populatsioon(e:list,l:list):
    """Sisestage elanike arv ja kuvage linna nimi, kus on lähim elanikke"""
    arv=int(input("Sisestage elanike arv: "))
    erinev_ls=[]
    while arv<1:
        arv=int(input("Arv peab olema suurem kui 0: "))
    for i in e:
        erinevus=abs(i-arv) #muuda negatiivsed arvud positiivseteks
        erinev_ls.append(erinevus)
    min_erinevus=min(erinev_ls)
    print("Ligikaudne elanike arv selles linnas: ",l[erinev_ls.index(min_erinevus)])
    

def vähem(e:list,l:list):
    """Leia linnad, kus on vähem kui n elanikku"""
    n=int(input("Sisestage elanike arv: "))
    linna=[]
    while n<1:
        n=int(input("Arv peab olema suurem kui 0: "))
    for i in e:
        if n>i:
            elanik_index=e.index(i)
            linna.append(l[elanik_index])
    print("Nendes linnades on väiksem elanikkond: ",linna)


def oma_variant(e:list,l:list):
    print("Maksimaalne elanike arv:")
    print(min(e), l[e.index(min(e))])
    print("Minimaalne elanike arv:")
    print(max(e), l[e.index(max(e))])