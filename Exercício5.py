Inteiros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,20]
PAR = []
IMPAR = []
for i in Inteiros:
    if Inteiros [i-1]%2:
        IMPAR.append(Inteiros[i-1])
    else:
        PAR.append(Inteiros[i-1])    
print ("Números", Inteiros)
print ("Números Pares", PAR)
print ("Números Impares", IMPAR)