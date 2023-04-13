AlunosNotas = [['Ana', [6, 3, 8, 9]], ['Bruno', [5, 6, 8, 2]], ['Caio', [10, 7, 8, 9]], ["Daniel", [9, 9, 8, 7]], ["Eduardo", [3, 6, 7, 7]], ['Felipe', [5, 7, 4, 3]], ['Gabriela', [10, 9, 8, 10]], ['Helena', [2, 10, 9, 9]], ['Igor', [3, 5, 6, 4]], ['Joana', [10, 5, 4, 7]]]
media = []

for aluno in AlunosNotas:
    media = sum(aluno[1]) / len(aluno[1])
    if(media >= 7):
        print(aluno[0], 'foi aprovado com nota: ', media)
    else:
        print(aluno[0], 'foi reprovado com nota: ', media)


