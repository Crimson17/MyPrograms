abeceda = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
matrica = [[0 for x in range(5)] for y in range(5)]
listaSlovauRijeci = []
abecedaBezSlova = []
rijec = input("Unesite rijec koju zelite enkriptirati: ").lower()
g=0
h=0
j=0
k=0



for y in abeceda:
    if y in rijec:
        listaSlovauRijeci.append(y)
for c in listaSlovauRijeci:
    if g != 5 :
        matrica[h][g] = c
        g = g+1
    elif g == 5:
        g=0
        h=h+1
        matrica[h][g] = c
for v in abeceda:
    if v not in matrica:
        if j != 5:
            matrica[k][j] = v
            j=j+1
        elif j == 5:
            j = 0
            k = k+1
            matrica[k][j] = v
print(matrica)