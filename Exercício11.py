lista_1 = [1,3,5,7,9,11,13,15,17,19]
lista_2 = [2,4,6,8,10,12,14,16,18,20]
lista_3 = ['A','B','C','D','E','F','G','H','I','J']
intercalado= []
for i in range(10):
    intercalado.append(lista_1[i])
    intercalado.append(lista_2[i])
    intercalado.append(lista_3[i])

print('Vetor A', lista_1)
print('Vetor B', lista_2)
print('Vetor C', lista_3)
print('Lista Intercalada',intercalado)