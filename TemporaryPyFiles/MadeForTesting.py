lista = [16, 51, 23, 255, 12, 67]

i = 1
j = 0

for i in range(len(lista)):
    for j in range(len(lista) - 1):
        if lista[i] > lista[j]:
            vab = lista[i]
            lista[i] = lista[j]
            lista[j] = vab

print(lista)
