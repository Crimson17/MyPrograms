abeceda = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ekripIliDekrip = int(input("Enkriptiranje(0) ili dekriptiranje(1)? "))
if ekripIliDekrip is 0:
    rijec = input("Unesi rijec koju zelis enkriptirati: ").lower()
    zelimrazmak = int(input("Zelite li sakriti razmake, Da = 1, Ne = 0?: "))
    kljuc = int(input("Unesite prvi broj kljuca: ")),int(input("Unesite drugi broj kljuca: "))
    kriplistaslova = []
    for x in rijec:
        if x.isspace() and zelimrazmak == 1:
            print("",end="")
        elif x.isspace() and zelimrazmak == 0:
            print(" ",end="")
        elif x in abeceda:
            print(abeceda[(kljuc[0]*int(abeceda.index(x))+kljuc[1]) % 26], end="")
        else:
            print("Uneseno:",x, "nije moguce enkriptirati, pokusajte ponovno.")

elif ekripIliDekrip is 1:
    print("dekr") #Wip
else:
    print(ekripIliDekrip, "nije niti 0 niti 1, idiote jedan.")