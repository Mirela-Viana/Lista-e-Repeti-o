ListaDOIS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ListaInvertida = []
for i in range (0,len(ListaDOIS)):
    ListaInvertida.append(ListaDOIS[len(ListaDOIS)-1])
    ListaDOIS.pop()
print(ListaInvertida)