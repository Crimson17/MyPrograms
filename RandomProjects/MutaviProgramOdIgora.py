import sys

najveciObrnutiBroj = 0             #Definiranje pocetnih varijabli
i = 1

while i % 10 != 0:
    i = int(input("Unesi prirodne brojeve: "))      #Unos prirodnih brojeva

    if i < 1:                                       #Provjera je li uneseni broj prirodan
        sys.exit("Uneseni broj nije prirodan.")

    stopTestiranja = 1                     #Definiranje ostalih varijabli
    brojTestiranja = 10
    brojacZnamenki = 0

    while stopTestiranja != 0:                          #Odredivanje broja znamenki unesenog prirodnog broja
        if i > brojTestiranja:
            brojTestiranja = brojTestiranja * 10
            brojacZnamenki = brojacZnamenki + 1
        else:
            brojacZnamenki = brojacZnamenki + 1
            stopTestiranja = 0

    potencijaBroja = brojacZnamenki                 #Opet malo varijabli
    obrnutiBroj = 0
    k = i

    for j in range(brojacZnamenki):                                         #Zamjena znamenki broja
        potencijaBroja = potencijaBroja - 1
        obrnutiBroj = obrnutiBroj + ((k % 10) * (10 ** potencijaBroja))
        k = k // 10

    if obrnutiBroj > najveciObrnutiBroj:                #Provjera najveceg obrnutog broja
        najveciObrnutiBroj = obrnutiBroj

print(najveciObrnutiBroj)               #Ispis najveceg obrnutog broja
