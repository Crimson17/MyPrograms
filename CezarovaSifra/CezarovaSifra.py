abeceda = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#abecedaDic = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,
#              "r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}       WIP
enkrilidekr = input("Enkriptiranje(0) ili Dekrptiranje(1)?: ")  #Provjerava sto zelis
enkrlista = []
blokada = 0
if enkrilidekr is 0:
    zelimspace = int(input("Zelis li da sakrijem razmake?, 1 = da, 0 = ne: "))
    rijec = input("Unesi rijec koju zelis enkriptirati: ")          #Inputi
    kljuc = int(input("Unesi broj kljuca: "))
    for x in range(len(rijec)): #Ispisuje slova redom
        slovo = rijec[x]
        if slovo in abeceda: #Provjerava ima li to slovo u abecedi
            enkrbroj = (kljuc + int(abeceda.index(slovo))) % 26
            enkrlista.append(str(abeceda[enkrbroj]))
        elif slovo == " " and zelimspace == 0:
            enkrlista.append(" ")                  #Ovo su dijelovi za space
        elif slovo == " " and zelimspace == 1:
            continue
        elif slovo not in abeceda:
            print("Uneseno slovo nije ispravno. Pokusaj ponovo") #U slucaju da nema slova u abecedi
            blokada = 1
    for h in enkrlista:  #Ispisuje enkriptiranu listu na kraju
        if blokada != 1:  #Blokada ako slovo nije u abecedi
            print(h, end="")

elif enkrilidekr is 1:
    listaslova = []
    rijec = input("Unesi rijec koju zelis dekriptirati: ")  #Input
    #for x in abeceda:
    #    v = rijec.count(x)                 WIP
    #    if v != 0:                         WIP
    #        abecedaDic[x] = int(v)
    for y in range(len(rijec)):
        slovo = rijec[y]
        listaslova.append(slovo)
    for c in range(26):
        print("")
        desiflista = []
        for b in listaslova:
            if b == " ":
                desiflista.append(" ")
            else:
                desifslovo = abeceda[(int(abeceda.index(b))-int(c)) % 26]
                desiflista.append(desifslovo)
        for m in desiflista:
            print(m, end="")
else:
    print(enkrilidekr,  "nije niti 0 niti 1, idiote jedan.")