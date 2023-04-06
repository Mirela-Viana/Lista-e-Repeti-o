notas = [3,5,8,10]
media = 0.0
alunos= ['Ana', 'Carol', 'Monica', 'Paulo']
print(notas[0])
for valorindex in notas:
    media= media + valorindex
media= media / len(notas)
print(media)