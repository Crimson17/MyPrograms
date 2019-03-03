abeceda = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ekripIliDekrip = input("Enkriptiranje(0) ili dekriptiranje(1)? ")
if ekripIliDekrip is 0:
    rijec = input("Unesi rijec koju zelis enkriptirati: ")
    for x in rijec:
        print(x)

elif ekripIliDekrip is 1:
    print("dekr") #Wip
else:
    print(ekripIliDekrip, "nije niti 0 niti 1, idiote jedan.")