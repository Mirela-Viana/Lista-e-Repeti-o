Idade =[]
Altura = []
IdadeInvertida= []
AlturaInvertida = []

for i in range(5):
    print('insira um valor Idade:')
    Idade.append(input())
print(Idade)

for i in range(5):
    print('insira um valor Altura:')
    Altura.append(input())
print(Altura)

for i in range (5):
   IdadeInvertida.append(Idade[len(Idade)-1])
   Idade.pop()
print ("Idade invertida", IdadeInvertida)

for i in range (5):
    AlturaInvertida.append(Altura[len(Altura)-1])
    Altura.pop()
print ("Altura invertida",AlturaInvertida)


