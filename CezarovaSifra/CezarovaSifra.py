abeceda = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
enkrilidekr = int(input("Enkriptiranje(0) ili dekrpitiranje(1)?: "))  #Provjerava sto zelis
enkrlista = []
blokada = 0
if enkrilidekr == 0:
    zelimspace = int(input("Zelis li da sakrijem razmake?, 0 = da, 1 = ne: "))
    rijec = input("Unesi rijec koju zelis enkriptirati: ")          #Inputi
    kljuc = int(input("Unesi broj kljuca: "))
    for x in range(len(rijec)): #Ispisuje slova redom
        slovo = rijec[x]
        if slovo in abeceda: #Provjerava ima li to slovo u abecedi
            enkrbroj = kljuc + int(abeceda.index(slovo))
            if enkrbroj > -1 and enkrbroj < 26: #Provjerava mora li koristiti modul
                enkrlista.append(str(abeceda[enkrbroj]))
            else:
                enkrbroj = enkrbroj % 26   #Koristi modul
                enkrlista.append(str(abeceda[enkrbroj]))
        elif slovo == " " and zelimspace == 1:
            enkrlista.append(" ")                  #Ovo su dijelovi za space
        elif slovo == " " and zelimspace == 0:
            continue
        elif slovo not in abeceda:
            print("Uneseno slovo nije ispravno. Pokusaj ponovo") #U slucaju da nema slova u abecedi
            blokada = 1
    for h in enkrlista:  #Ispisuje enkriptiranu listu na kraju
        if blokada != 1:  #Blokada ako slovo nije u abecedi
            print(h, end="")

elif enkrilidekr == 1:
    rijec = input("Unesi rijec koju zelis dekriptirati: ")  #Input

    for x in range(len(rijec)):
        print("VIP")
else:
    print("Nisi unjeo tocan broj.")