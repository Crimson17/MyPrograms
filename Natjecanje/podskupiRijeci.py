import sys

pocetnaRijec = str(input()).upper()
if len(pocetnaRijec) >= 3 and len(pocetnaRijec) <= 20:
    brojKandidata = int(input())
    if brojKandidata >= 2 and brojKandidata <= 6:
        for i in range(brojKandidata):
            print("WIP")
else:
    sys.exit()