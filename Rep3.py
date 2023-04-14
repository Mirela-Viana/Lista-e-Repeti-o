print('Insira seu nome')
nome=input()
while len(nome) < 3:
    print("Nome com mais de três caracteres:")
    nome=input()

print('Insira sua Idade:')
idade=int(input())
while idade <0 or idade> 150:
    print('Insira sua idade corretamente:')
    idade=int(input())

print('Insira seu salário')
salario=int(input())
while salario <= 0:
    print("Insira o salário corretamente:")
    salario=int(input())

print('Insira seu sexo/genêro: f ou m')
sexo=input()
while sexo != "f" and sexo != "m":
    print('genêro invalido:')
    sexo=input()

print('Insira seu Estado civil: s, c, v ou d:')
estado=input()
while estado != "s" and estado != "c" and estado != "v" and estado != "d":
    print('Estado civil invalido')
    estado=input()
