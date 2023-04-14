Lista_1 = [1,3,5,7,9,11,13,15,17,19]
Lista_2 = [2,4,6,8,10,12,14,16,18,20]
intercalado= []
for i in range(10):
    intercalado.append(Lista_1[i])
    intercalado.append(Lista_2[i])

print('Vetor A', Lista_1)
print('Vetor B', Lista_2)
print('Lista Intercalada',intercalado)
