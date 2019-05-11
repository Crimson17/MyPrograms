import os


path = r"C:\Users\Ivan\Documents\GitHub\MyPrograms"

blokada = 0

listaFajlova = []

for r, d, f in os.walk(path):
    for file in f:
        if file.endswith(".py"):
            listaFajlova.append(file)

for c in listaFajlova:
    print(listaFajlova.index(c), c)

odabir = int(input("Odaberi file(Broj ispred): "))

if odabir < 0 or odabir > len(listaFajlova)-1:
    print("Upisao si krivi broj idiote..")
    blokada = 1

if blokada == 0:
    destinacija = r(input("Unesi destinacju exe-a: "))
