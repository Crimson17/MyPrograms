abeceda = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#abecedaDic = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,
#              "r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}       WIP
enkrilidekr = int(input("Enkriptiranje(0) ili Dekrptiranje(1)?: "))
enkrlista = []
blokada = 0
blokada2 = 0
blokada3 = 0
if enkrilidekr == 0:
    zelimspace = int(input("Zelite li sakriti razmake?, 1 = da, 0 = ne: "))
    if zelimspace != 0 and zelimspace != 1:
        print(zelimspace, "nije niti 0 niti 1.")
        blokada2 = 1
    if blokada2 == 0:
        rijec = input("Unesite rijec koju zelite enkriptirati: ").lower()
        kljuc = int(input("Unesite broj kljuca: "))
        for x in rijec:
            if x in abeceda:
                print(abeceda[(kljuc + int(abeceda.index(x))) % 26], end="")
            elif x == " " and zelimspace == 0:
                print(" ",end="")
            elif x == " " and zelimspace == 1:
                print("",end="")
            elif x not in abeceda:
                print("Uneseno slovo nije ispravno. Pokusajte ponovno")
                blokada = 1
            if blokada != 0:
                break

elif enkrilidekr == 1:
    rijec = input("Unesite rijec koju zelite dekriptirati: ").lower()
    for c in range(26):
        print("")
        for b in rijec:
            if b == " ":
                print(" ", end="")
            elif b in abeceda:
                print(abeceda[(int(abeceda.index(b))-int(c)) % 26], end="")
            else:
                print("Unos:",b,"nije ispravan.")
                blokada3 = 1
        if blokada3 != 0:
            break

else:
    print(enkrilidekr,  "nije niti 0 niti 1.")
stopiranje = input("\npress any key to exit...")
