Alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
Vogais = ['A', 'E', 'I','O','U']
ListaSeparada = []
Contador = 0
Consoantes = 0
for i in Alfabeto:
    if not Alfabeto[Contador] in Vogais:
        Consoantes += 1
        ListaSeparada.append (Alfabeto[Contador])
    Contador += 1
print ("Letras", Alfabeto)
print ("Consoantes", ListaSeparada) 
print (Consoantes)