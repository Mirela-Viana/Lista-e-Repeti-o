notas = [3,5,8,10]
media = 0.0
print('Notas', notas)
for valorindex in notas:
    media= media + valorindex
media= media / len(notas)
print('Média', media)